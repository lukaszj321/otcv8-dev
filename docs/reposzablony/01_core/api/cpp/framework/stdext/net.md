---
doc_id: "cpp-api-9563d2415832"
source_path: "framework/stdext/net.h"
source_sha: "b411fa2"
last_sync_iso: "2025-10-09T07:28:40Z"
doc_class: "api"
language: "pl"
title: "API: net.h"
summary: "Dokumentacja API C++ dla framework/stdext/net.h"
tags: ["cpp", "api", "otclient"]
---

# framework/stdext/net.h

## Overview

Plik nagłówkowy C++ zawierający definicje dla modułu net.

## Namespaces

### `stdext`

## Functions

### `ip_to_string`

**Sygnatura:** `std::string ip_to_string(uint32 ip)`

### `string_to_ip`

**Sygnatura:** `uint32 string_to_ip(const std::string& string)`

### `listSubnetAddresses`

**Sygnatura:** `std::vector<uint32> listSubnetAddresses(uint32 address, uint8 mask)`
