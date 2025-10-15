-- docio.lua (improved)
local docio = {}
docio.MAX_BYTES = 50 * 1024 * 1024

local function as_lf(s) return (tostring(s or ""):gsub("\r\n", "\n"):gsub("\r", "\n")) end

local function dirname(path)
  local sep = package.config:sub(1, 1)
  return path:match("^(.*" .. sep .. ")") and path:match("^(.*" .. sep .. ")"):sub(1, -2) or "."
end

local function mkdir_p(dir)
  if dir == "" or dir == "." or not dir then return true end
  local sep = package.config:sub(1, 1)
  local parts = {}
  for part in string.gmatch(dir, "[^" .. sep .. "]+") do table.insert(parts, part) end
  local acc = ""
  for i = 1, #parts do
    acc = (acc == "") and parts[i] or (acc .. sep .. parts[i])
    local cmd
    if sep == "\\" then
      cmd = string.format(
      'powershell -NoProfile -Command "New-Item -ItemType Directory -Force -Path \\"%s\\" | Out-Null"', acc)
    else
      cmd = string.format('mkdir -p "%s"', acc)
    end
    os.execute(cmd)
  end
  return true
end

function docio.writeAll(path, content)
  mkdir_p(dirname(path))
  local f, err = io.open(path, "wb")
  assert(f, "Cannot open for write: " .. tostring(err))
  f:write(as_lf(content))
  f:close()
end

function docio.readAll(path)
  local f = io.open(path, "rb")
  if not f then return nil end
  local s = f:read("*all")
  f:close()
  return s
end

function docio.append(path, content)
  mkdir_p(dirname(path))
  local f, err = io.open(path, "ab")
  assert(f, "Cannot open for append: " .. tostring(err))
  f:write(as_lf(content))
  f:close()
end

function docio.fileSize(path)
  local f = io.open(path, "rb")
  if not f then return 0 end
  local sz = f:seek("end")
  f:close()
  return sz or 0
end

function docio.needsRotation(path)
  return docio.fileSize(path) >= docio.MAX_BYTES
end

function docio.rotate(path)
  local sep = package.config:sub(1, 1)
  local dir = dirname(path)
  local base = path:match("[^" .. sep .. "]+$") or path
  local name, ext = base:match("(.+)%.([^%.]+)$")
  if not name then name, ext = base, "" end
  local chunkDir = dir .. sep .. "chunks"
  mkdir_p(chunkDir)
  local ts = os.date("!%Y%m%d-%H%M%S")
  local newPath = chunkDir .. sep .. name .. "." .. ts .. (ext ~= "" and "." .. ext or "")
  os.rename(path, newPath)
  return newPath
end

local function csv_escape(v)
  local s = tostring(v or "")
  s = s:gsub('"', '""')
  if s:find('[,"\n]') then s = '"' .. s .. '"' end
  return s
end

function docio.writeCSV(path, headers, rows)
  if docio.needsRotation(path) then docio.rotate(path) end
  local out = {}
  out[#out + 1] = table.concat(headers, ",")
  for _, row in ipairs(rows or {}) do
    local line = {}
    for _, h in ipairs(headers) do
      local val = row[h]
      if type(val) == "table" then
        local tmp = {}
        for i, v in ipairs(val) do tmp[i] = tostring(v) end
        val = table.concat(tmp, "|")
      end
      line[#line + 1] = csv_escape(val)
    end
    out[#out + 1] = table.concat(line, ",")
  end
  docio.writeAll(path, table.concat(out, "\n") .. "\n")
end

function docio.writeNDJSON(path, records)
  if docio.needsRotation(path) then docio.rotate(path) end
  local ok, json = pcall(require, "dkjson")
  if not ok then ok, json = pcall(require, "cjson") end
  if not ok then ok, json = pcall(require, "json") end
  assert(ok and json and (json.encode or json.encode_sparse_array), "No JSON lib found (dkjson/cjson/json)")
  local enc = json.encode or json.encode_sparse_array
  local lines = {}
  for _, rec in ipairs(records or {}) do
    lines[#lines + 1] = enc(rec)
  end
  docio.writeAll(path, table.concat(lines, "\n") .. "\n")
end

function docio.isoTimestamp() return os.date("!%Y-%m-%dT%H:%M:%SZ") end

return docio
