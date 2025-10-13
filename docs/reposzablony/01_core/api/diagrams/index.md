# Diagrams


## Diagrams

```{mermaid}
:caption: Adaptiverenderer

classDiagram
    class AdaptiveRenderer {
    }
```

```{mermaid}
:caption: Android Native App Glue

classDiagram
    class android_app {
    }
    class android_poll_source {
    }
    class android_app {
    }
    class android_app {
    }
    class android_poll_source {
    }
    class android_poll_source {
    }
```

```{mermaid}
:caption: Androidwindow

classDiagram
    class AndroidWindow {
    }
```

```{mermaid}
:caption: Animatedtext

classDiagram
    class AnimatedText {
        +drawText()
        +setColor()
        +setText()
        +setOffset()
        +setFont()
        +getColor()
        +getOffset()
        +getTimer()
        +merge()
        +asAnimatedText()
        +isAnimatedText()
        +getText()
        #onAppear()
    }
```

```{mermaid}
:caption: Animatedtexture

classDiagram
    class AnimatedTexture {
        +replace()
        +update()
        +isAnimatedTexture()
        #buildHardwareMipmaps()
        #setSmooth()
        #setRepeat()
    }
```

```{mermaid}
:caption: Animator

classDiagram
    class Animator {
        +unserialize()
        +serialize()
        +setPhase()
        +getPhase()
        +getPhaseAt()
        +getStartPhase()
        +getAnimationPhases()
        +isAsync()
        +isComplete()
        +getTotalDuration()
        +resetAnimation()
    }
```

```{mermaid}
:caption: Any

classDiagram
    class any {
    }
    class placeholder {
    }
    class holder {
    }
```

```{mermaid}
:caption: Apngloader

classDiagram
    class apng_data {
    }
```

```{mermaid}
:caption: Application

classDiagram
    class Application {
        +init()
        +deinit()
        +terminate()
        +run()
        +poll()
        +exit()
        +quick_exit()
        +close()
        +restart()
        +restartArgs()
        +setName()
        +setCompactName()
        +setVersion()
        +isRunning()
        +isStopping()
        +isTerminated()
        +getCharset()
        +getBuildCompiler()
        +getBuildDate()
        +getBuildRevision()
        ... (19 more members)
    }
```

```{mermaid}
:caption: Asyncdispatcher

classDiagram
    class AsyncDispatcher {
    }
```

```{mermaid}
:caption: Atlas

classDiagram
    class Atlas {
    }
```

```{mermaid}
:caption: Binarytree

classDiagram
    class BinaryTree {
        +seek()
        +skip()
        +tell()
        +size()
        +getU8()
        +getU16()
        +getU32()
        +getU64()
        +getString()
        +getPoint()
        +getChildren()
        +canRead()
    }
    class OutputBinaryTree {
        +addU8()
        +addU16()
        +addU32()
        +addString()
        +addPos()
        +addPoint()
        +startNode()
        +endNode()
        #write()
    }
```

```{mermaid}
:caption: Bitmapfont

classDiagram
    class BitmapFont {
        +load()
        +drawText()
        +drawText()
        +drawColoredText()
        +calculateDrawTextCoords()
        +align
        +calculateTextRectSize()
        +wrapText()
        +getId()
        +getName()
        +getGlyphHeight()
        +getYOffset()
        +getGlyphSpacing()
    }
```

```{mermaid}
:caption: Boolean

classDiagram
    class boolean {
    }
```

```{mermaid}
:caption: Cachedtext

classDiagram
    class CachedText {
        +draw()
        +wrapText()
        +setFont()
        +setText()
        +setColoredText()
        +setAlign()
        +getTextSize()
        +getText()
        +getFont()
        +getAlign()
        +hasText()
    }
```

```{mermaid}
:caption: Cast

classDiagram
    class cast_exception {
    }
```

```{mermaid}
:caption: Client

classDiagram
    class Client {
        +init()
        +terminate()
        +registerLuaFunctions()
    }
```

```{mermaid}
:caption: Clock

classDiagram
    class Clock {
        +update()
        +micros()
        +millis()
        +seconds()
        +realMicros()
        +realMillis()
    }
```

```{mermaid}
:caption: Color

classDiagram
    class Color {
        +a()
        +b()
        +g()
        +r()
        +aF()
        +bF()
        +gF()
        +rF()
        +setRed()
        +setGreen()
        +setBlue()
        +setAlpha()
        +setRed()
        +setGreen()
        +setBlue()
        +setAlpha()
        +setRGBA()
        +setRGBA()
        +opacity()
        +Color()
        ... (14 more members)
    }
```

```{mermaid}
:caption: Colorarray

classDiagram
    class ColorArray {
        +addColor()
        +addColor()
        +clear()
        +colorCount()
        +count()
        +size()
    }
```

```{mermaid}
:caption: Combinedsoundsource

classDiagram
    class CombinedSoundSource {
        +addSource()
        +getSources()
        +play()
        +stop()
        +isBuffering()
        +isPlaying()
        +setLooping()
        +setRelative()
        +setReferenceDistance()
        +setGain()
        +setPitch()
        +setPosition()
        +setVelocity()
        +setFading()
        #update()
    }
```

```{mermaid}
:caption: Config

classDiagram
    class Config {
        +load()
        +unload()
        +save()
        +clear()
        +setValue()
        +setList()
        +getValue()
        +getList()
        +setNode()
        +mergeNode()
        +getNode()
        +getNodeSize()
        +exists()
        +remove()
        +getFileName()
        +isLoaded()
        +asConfig()
    }
```

```{mermaid}
:caption: Configmanager

classDiagram
    class ConfigManager {
        +init()
        +terminate()
        +getSettings()
        +get()
        +create()
        +loadSettings()
        +load()
        +unload()
        +remove()
        #m_settings
    }
```

```{mermaid}
:caption: Connection

classDiagram
    class Connection {
        +poll()
        +terminate()
        +connect()
        +close()
        +write()
        +read()
        +read_until()
        +read_some()
        +setErrorCallback()
        +getIp()
        +getError()
        +isConnecting()
        +isConnected()
        +getElapsedTicksSinceLastRead()
        +asConnection()
        #internal_connect()
        #internal_write()
        #onResolve()
        #onConnect()
        #onCanWrite()
        ... (18 more members)
    }
```

```{mermaid}
:caption: Consoleapplication

classDiagram
    class ConsoleApplication {
        +run()
    }
```

```{mermaid}
:caption: Container

classDiagram
    class Container {
        +getItem()
        +getItems()
        +getItemsCount()
        +getSlotPosition()
        +getId()
        +getCapacity()
        +getContainerItem()
        +getName()
        +hasParent()
        +isClosed()
        +isUnlocked()
        +hasPages()
        +getSize()
        +getFirstIndex()
        +findItemById()
        #onOpen()
        #onClose()
        #onAddItem()
        #onAddItems()
        #onUpdateItem()
        ... (1 more members)
    }
```

```{mermaid}
:caption: Coordsbuffer

classDiagram
    class CoordsBuffer {
        +clear()
        +addTriangle()
        +addRect()
        +addRect()
        +addRect()
        +addQuad()
        +addUpsideDownQuad()
        +addBoudingRect()
        +addRepeatedRects()
        +getVertexCount()
        +getTextureCoordCount()
        +unlock()
        +cache()
        +getTextureRect()
    }
```

```{mermaid}
:caption: Creature

classDiagram
    class Creature {
        +draw()
        +drawOutfit()
        +drawInformation()
        +isInsideOffset()
        +setId()
        +setName()
        +setManaPercent()
        +setHealthPercent()
        +setDirection()
        +setOutfit()
        +setOutfitColor()
        +setLight()
        +setSpeed()
        +setBaseSpeed()
        +setSkull()
        +setShield()
        +setEmblem()
        +setType()
        +setIcon()
        +setSkullTexture()
        ... (175 more members)
    }
    class Npc {
        +isNpc()
    }
    class Monster {
        +isMonster()
    }
```

```{mermaid}
:caption: Creatures

classDiagram
    class Spawn {
        +setRadius()
        +getRadius()
        +setCenterPos()
        +getCenterPos()
        +getCreatures()
        +addCreature()
        +removeCreature()
        +clear()
        #load()
        #save()
    }
    class CreatureType {
        +setSpawnTime()
        +getSpawnTime()
        +setName()
        +getName()
        +setOutfit()
        +getOutfit()
        +setDirection()
        +getDirection()
        +setRace()
        +getRace()
        +cast()
    }
    class CreatureManager {
        +clear()
        +clearSpawns()
        +terminate()
        +loadMonsters()
        +loadSingleCreature()
        +loadNpcs()
        +loadCreatureBuffer()
        +loadSpawns()
        +saveSpawns()
        +getSpawns()
        +getSpawn()
        +getSpawnForPlacePos()
        +addSpawn()
        +deleteSpawn()
        +isLoaded()
        +isSpawnLoaded()
        #internalLoadCreatureBuffer()
    }
```

```{mermaid}
:caption: Crypt

classDiagram
    class Crypt {
        +base64Encode()
        +base64Decode()
        +xorCrypt()
        +encrypt()
        +decrypt()
        +genUUID()
        +setMachineUUID()
        +getMachineUUID()
        +md5Encode()
        +sha1Encode()
        +sha256Encode()
        +sha512Encode()
        +crc32()
        +rsaGenerateKey()
        +rsaSetPublicKey()
        +rsaSetPrivateKey()
        +rsaCheckKey()
        +rsaEncrypt()
        +rsaDecrypt()
        +rsaGetSize()
        ... (2 more members)
    }
```

```{mermaid}
:caption: Databuffer

classDiagram
    class DataBuffer {
        +reset()
        +clear()
        +empty()
        +size()
        +reserve()
        +resize()
        +grow()
        +newcapacity
        +add()
    }
```

```{mermaid}
:caption: Declarations

classDiagram
    class UIManager {
    }
    class UIWidget {
    }
    class UITextEdit {
    }
    class UILayout {
    }
    class UIBoxLayout {
    }
    class UIHorizontalLayout {
    }
    class UIVerticalLayout {
    }
    class UIGridLayout {
    }
    class UIAnchor {
    }
    class UIAnchorGroup {
    }
    class UIAnchorLayout {
    }
```

```{mermaid}
:caption: Deptharray

classDiagram
    class DepthArray {
        +addDepth()
        +clear()
        +depthCount()
        +count()
        +size()
    }
```

```{mermaid}
:caption: Drawcache

classDiagram
    class DrawCache {
    }
```

```{mermaid}
:caption: Drawqueue

classDiagram
    class DrawQueue {
    }
    class DrawQueueItem {
    }
    class DrawQueueItem {
    }
    class DrawQueueItemTexturedRect {
    }
    class DrawQueueItemTextureCoords {
    }
    class DrawQueueItemColoredTextureCoords {
    }
    class DrawQueueItemImageWithShader {
    }
    class DrawQueueItemFilledRect {
    }
    class DrawQueueItemClearRect {
    }
    class DrawQueueItemFillCoords {
    }
    class DrawQueueItemText {
    }
    class DrawQueueItemTextColored {
    }
    class DrawQueueItemLine {
    }
    class DrawQueueCondition {
    }
    class DrawQueueConditionClip {
    }
    class DrawQueueConditionRotation {
    }
    class DrawQueueConditionMark {
    }
    class DrawQueue {
    }
```

```{mermaid}
:caption: Dumper

classDiagram
    class dumper_dummy {
    }
```

```{mermaid}
:caption: Dynamic Storage

classDiagram
    class dynamic_storage {
    }
```

```{mermaid}
:caption: Effect

classDiagram
    class Effect {
        +draw()
        +draw()
        +setId()
        +getId()
        +asEffect()
        +isEffect()
        #onAppear()
    }
```

```{mermaid}
:caption: Event

classDiagram
    class Event {
        +execute()
        +cancel()
        +isCanceled()
        +isExecuted()
        +isBotSafe()
        #m_function
        #m_callback
        #m_canceled
        #m_executed
        #m_botSafe
    }
```

```{mermaid}
:caption: Eventdispatcher

classDiagram
    class EventDispatcher {
        +shutdown()
        +poll()
        +addEventEx()
        +scheduleEventEx()
        +cycleEventEx()
        +isBotSafe()
    }
```

```{mermaid}
:caption: Exception

classDiagram
    class exception {
        #m_what
    }
```

```{mermaid}
:caption: Extras

classDiagram
    class Extras {
    }
```

```{mermaid}
:caption: Filestream

classDiagram
    class PHYSFS_File {
        +close()
        +flush()
        +write()
        +read()
        +seek()
        +skip()
        +size()
        +tell()
        +eof()
        +name()
        +getU8()
        +getU16()
        +getU32()
        +getU64()
        +get8()
        +get16()
        +get32()
        +get64()
        +getString()
        +getBinaryTree()
        ... (14 more members)
    }
    class FileStream {
        +close()
        +flush()
        +write()
        +read()
        +seek()
        +skip()
        +size()
        +tell()
        +eof()
        +name()
        +getU8()
        +getU16()
        +getU32()
        +getU64()
        +get8()
        +get16()
        +get32()
        +get64()
        +getString()
        +getBinaryTree()
        ... (14 more members)
    }
```

```{mermaid}
:caption: Fontmanager

classDiagram
    class FontManager {
        +terminate()
        +clearFonts()
        +importFont()
        +fontExists()
        +getFont()
        +getDefaultFont()
        +setDefaultFont()
    }
```

```{mermaid}
:caption: Framebuffer

classDiagram
    class FrameBuffer {
        +resize()
        +bind()
        +release()
        +draw()
        +draw()
        +draw()
        +setSmooth()
        +getTexture()
        +getSize()
        +isSmooth()
        +getDepthRenderBuffer()
        +hasDepth()
        +readPixels()
        +doScreenshot()
    }
```

```{mermaid}
:caption: Framebuffermanager

classDiagram
    class FrameBufferManager {
        +init()
        +terminate()
        +clear()
        +createFrameBuffer()
        #m_temporaryFramebuffer
        #m_drawQueueTemporaryFramebuffer
        #m_framebuffers
    }
```

```{mermaid}
:caption: Framecounter

classDiagram
    class FrameCounter {
    }
```

```{mermaid}
:caption: Game

classDiagram
    class UnjustifiedPoints {
    }
    class Game {
        +init()
        +terminate()
        #processConnectionError()
        #processDisconnect()
        #processPing()
        #processPingBack()
        #processNewPing()
        #processUpdateNeeded()
        #processLoginError()
        #processLoginAdvice()
        #processLoginWait()
        #processLoginToken()
        #processLogin()
        #processPendingGame()
        #processEnterGame()
        #processGameStart()
        #processGameEnd()
        #processDeath()
        #processGMActions()
        #processInventoryChange()
        ... (205 more members)
    }
```

```{mermaid}
:caption: Graph

classDiagram
    class Graph {
        +draw()
        +clear()
        +addValue()
    }
```

```{mermaid}
:caption: Graphicalapplication

classDiagram
    class GraphicalApplication {
        +init()
        +deinit()
        +terminate()
        +run()
        +poll()
        +pollGraphics()
        +close()
        +willRepaint()
        +repaint()
        +setMaxFps()
        +getMaxFps()
        +getFps()
        +getGraphicsFps()
        +getProcessingFps()
        +isOnInputEvent()
        +getIteration()
        +m_iteration
        +doScreenshot()
        +scaleUp()
        +scaleDown()
        ... (5 more members)
    }
```

```{mermaid}
:caption: Graphics

classDiagram
    class Painter {
        +init()
        +terminate()
        +resize()
        +checkDepthSupport()
        +getMaxTextureSize()
        +getVendor()
        +getRenderer()
        +getVersion()
        +getExtensions()
        +ok()
        +checkForError()
    }
    class Graphics {
        +init()
        +terminate()
        +resize()
        +checkDepthSupport()
        +getMaxTextureSize()
        +getVendor()
        +getRenderer()
        +getVersion()
        +getExtensions()
        +ok()
        +checkForError()
    }
```

```{mermaid}
:caption: Hardwarebuffer

classDiagram
    class HardwareBuffer {
        +bind()
        +unbind()
        +write()
    }
```

```{mermaid}
:caption: Healthbars

classDiagram
    class HealthBar {
        +setPath()
        +getPath()
        +setTexture()
        +getTexture()
        +setOffset()
        +getOffset()
        +setBarOffset()
        +getBarOffset()
        +setHeight()
        +getHeight()
    }
    class HealthBars {
        +init()
        +terminate()
        +addHealthBackground()
        +addManaBackground()
        +getHealthBar()
        +getManaBar()
        +getHealthBarPath()
        +getManaBarPath()
        +getHealthBarOffset()
        +getManaBarOffset()
        +getHealthBarOffsetBar()
        +getManaBarOffsetBar()
        +getHealthBarHeight()
        +getManaBarHeight()
    }
```

```{mermaid}
:caption: Houses

classDiagram
    class House {
        +setTile()
        +getTile()
        +setName()
        +getName()
        +setId()
        +getId()
        +setTownId()
        +getTownId()
        +setSize()
        +getSize()
        +setRent()
        +getRent()
        +setEntry()
        +getEntry()
        +addDoor()
        +removeDoor()
        +removeDoorById()
        #load()
        #save()
    }
    class HouseManager {
    }
```

```{mermaid}
:caption: Http

classDiagram
    class WebsocketSession {
        +init()
        +terminate()
        +get()
        +post()
        +download()
        +ws()
        +wsSend()
        +wsClose()
        +cancel()
        +m_downloads
        +clearDownloads()
        +getFile()
        +it
        +nullptr
        +setUserAgent()
    }
    class Http {
    }
```

```{mermaid}
:caption: Image

classDiagram
    class Image {
        +load()
        +loadPNG()
        +loadPNG()
        +savePNG()
        +blit()
        +paste()
        +upscale()
        +resize()
        +nextMipmap()
        +setPixel()
        +setPixel()
        +setPixel()
        +getPixelCount()
        +getWidth()
        +getHeight()
        +getBpp()
        +fromQRCode()
    }
```

```{mermaid}
:caption: Inputevent

classDiagram
    class InputEvent {
    }
```

```{mermaid}
:caption: Inputmessage

classDiagram
    class InputMessage {
        +setBuffer()
        +getBuffer()
        +getBodyBuffer()
        +skipBytes()
        +setReadPos()
        +getU8()
        +getU16()
        +getU32()
        +getU64()
        +getString()
        +getDouble()
        +peekU8()
        +peekU16()
        +peekU32()
        +peekU64()
        +decryptRsa()
        +getHeaderPos()
        +getHeaderSize()
        +getReadSize()
        +getReadPos()
        ... (10 more members)
    }
```

```{mermaid}
:caption: Item

classDiagram
    class Item {
        +create()
        +createFromOtb()
        +draw()
        +draw()
        +setId()
        +setOtbId()
        +setCountOrSubType()
        +setCount()
        +setSubType()
        +setColor()
        +setTooltip()
        +setQuickLootFlags()
        +setShader()
        +getCountOrSubType()
        +getSubType()
        +getCount()
        +getId()
        +getClientId()
        +getServerId()
        +getName()
        ... (42 more members)
    }
```

```{mermaid}
:caption: Itemtype

classDiagram
    class ItemType {
        +unserialize()
        +setServerId()
        +getServerId()
        +setClientId()
        +getClientId()
        +setCategory()
        +getCategory()
        +setName()
        +getName()
        +setDesc()
        +getDesc()
        +isNull()
        +isWritable()
    }
```

```{mermaid}
:caption: Lbitlib

classDiagram
    class lua_State {
    }
```

```{mermaid}
:caption: Lightview

classDiagram
    class TileLight {
    }
    class LightView {
        +addLight()
        +addLight()
        +addLight()
        +setFieldBrightness()
        +size()
        +draw()
    }
```

```{mermaid}
:caption: Localplayer

classDiagram
    class LocalPlayer {
        +draw()
        +unlockWalk()
        +lockWalk()
        +stopAutoWalk()
        +autoWalk()
        +canWalk()
        +isWalkLocked()
        +turn()
        +setStates()
        +setSkill()
        +setBaseSkill()
        +setHealth()
        +setFreeCapacity()
        +setTotalCapacity()
        +setExperience()
        +setLevel()
        +setMana()
        +setMagicLevel()
        +setBaseMagicLevel()
        +setSoul()
        ... (64 more members)
    }
```

```{mermaid}
:caption: Logger

classDiagram
    class LogMessage {
    }
    class Logger {
        +log()
        +logFunc()
        +debug()
        +info()
        +warning()
        +error()
        +fatal()
        +fireOldMessages()
        +setLogFile()
        +setOnLog()
        +getLastLog()
        +m_lastLog
        +setTestingMode()
    }
```

```{mermaid}
:caption: Luabinder

classDiagram
    class pack_values_into_tuple {
    }
    class pack_values_into_tuple {
    }
    class expand_fun_arguments {
    }
    class expand_fun_arguments {
    }
    class bind_lambda_fun {
    }
    class bind_lambda_fun {
    }
```

```{mermaid}
:caption: Luaexception

classDiagram
    class LuaException {
        +generateLuaErrorMessage()
        #m_what
    }
    class LuaBadNumberOfArgumentsException {
    }
    class LuaBadValueCastException {
    }
```

```{mermaid}
:caption: Luainterface

classDiagram
    class lua_State {
        +init()
        +terminate()
        +registerFunctions()
        +registerSingletonClass()
        +registerClass()
        +registerClass()
        +registerClassStaticFunction()
        +registerClassMemberFunction()
        +bindSingletonFunction()
        +bindSingletonFunction()
        +bindSingletonFunction()
        +bindClassStaticFunction()
        +bindClassStaticFunction()
        +bindClassMemberFunction()
        +bindClassMemberFunction()
        +bindClassMemberField()
        +bindClassMemberField()
        +bindClassMemberGetField()
        +bindClassMemberGetField()
        +bindClassMemberSetField()
        ... (105 more members)
    }
    class LuaInterface {
        +init()
        +terminate()
        +registerFunctions()
        +registerSingletonClass()
        +registerClass()
        +registerClass()
        +registerClassStaticFunction()
        +registerClassMemberFunction()
        +bindSingletonFunction()
        +bindSingletonFunction()
        +bindSingletonFunction()
        +bindClassStaticFunction()
        +bindClassStaticFunction()
        +bindClassMemberFunction()
        +bindClassMemberFunction()
        +bindClassMemberField()
        +bindClassMemberField()
        +bindClassMemberGetField()
        +bindClassMemberGetField()
        +bindClassMemberSetField()
        ... (105 more members)
    }
```

```{mermaid}
:caption: Luaobject

classDiagram
    class LuaObject {
        +connectLuaField()
        +luaCallLuaField()
        +callLuaField()
        +callLuaField()
        +hasLuaField()
        +setLuaField()
        +getLuaField()
        +releaseLuaFieldsTable()
        +luaSetField()
        +luaGetField()
        +luaGetMetatable()
        +luaGetFieldsTable()
        +getUseCount()
        +getClassName()
        +asLuaObject()
        +operator
    }
    class connect_lambda {
    }
    class connect_lambda {
    }
```

```{mermaid}
:caption: Luavaluecasts

classDiagram
    class push_tuple_internal_luavalue {
    }
    class push_tuple_internal_luavalue {
    }
    class push_tuple_luavalue {
    }
    class push_tuple_luavalue {
    }
```

```{mermaid}
:caption: Map

classDiagram
    class TileBlock {
    }
    class AwareRange {
    }
    class PathFindResult {
    }
    class Node {
    }
    class Map {
        +init()
        +terminate()
        +addMapView()
        +removeMapView()
        +notificateTileUpdate()
        +requestVisibleTilesCacheUpdate()
        +loadOtcm()
        +saveOtcm()
        +loadOtbm()
        +saveOtbm()
        +setHouseFile()
        +setSpawnFile()
        +setDescription()
        +clearDescriptions()
        +setWidth()
        +setHeight()
        +getHouseFile()
        +getSpawnFile()
        +getSize()
        +getDescriptions()
        ... (58 more members)
    }
```

```{mermaid}
:caption: Mapview

classDiagram
    class MapView {
        +drawMapBackground()
        +drawMapForeground()
        #onTileUpdate()
        #onMapCenterChange()
        +lockFirstVisibleFloor()
        +unlockFirstVisibleFloor()
        +getLockedFirstVisibleFloor()
        +setMultifloor()
        +isMultifloor()
        +setVisibleDimension()
        +optimizeForSize()
        +getVisibleDimension()
        +getVisibleCenterOffset()
        +getCachedFirstVisibleFloor()
        +getCachedLastVisibleFloor()
        +followCreature()
        +getFollowingCreature()
        +isFollowingCreature()
        +setCameraPosition()
        +getCameraPosition()
        ... (25 more members)
    }
```

```{mermaid}
:caption: Matrix

classDiagram
    class Matrix {
        +setIdentity()
        +isIdentity()
        +fill()
        +transposed()
        +operator()
        +operator
    }
```

```{mermaid}
:caption: Minimap

classDiagram
    class MinimapTile {
    }
    class MinimapBlock {
        +clean()
        +update()
        +updateTile()
        +resetTile()
        +getTileIndex()
        +mustUpdate()
        +justSaw()
        +wasSeen()
    }
    class Minimap {
        +init()
        +terminate()
        +clean()
        +draw()
        +getTilePoint()
        +getTilePosition()
        +getTileRect()
        +updateTile()
        +threadGetTile()
        +loadImage()
        +saveImage()
        +loadOtmm()
        +saveOtmm()
    }
```

```{mermaid}
:caption: Missile

classDiagram
    class Missile {
        +draw()
        +setId()
        +setPath()
        +getId()
        +asMissile()
        +isMissile()
        +getSource()
        +getDestination()
    }
```

```{mermaid}
:caption: Module

classDiagram
    class Module {
        +load()
        +unload()
        +reload()
        +canUnload()
        +canReload()
        +isLoaded()
        +isReloadable()
        +isDependent()
        +isSandboxed()
        +hasDependency()
        +getSandbox()
        +getDescription()
        +getName()
        +getAuthor()
        +getWebsite()
        +getVersion()
        +isAutoLoad()
        +getAutoLoadPriority()
        +asModule()
        #discover()
    }
```

```{mermaid}
:caption: Modulemanager

classDiagram
    class ModuleManager {
        +clear()
        +discoverModules()
        +autoLoadModules()
        +discoverModule()
        +ensureModuleLoaded()
        +unloadModules()
        +reloadModules()
        +getModule()
        +getModules()
        #updateModuleLoadOrder()
    }
```

```{mermaid}
:caption: Mouse

classDiagram
    class Mouse {
        +init()
        +terminate()
        +loadCursors()
        +addCursor()
        +pushCursor()
        +popCursor()
        +isCursorChanged()
        +isPressed()
    }
```

```{mermaid}
:caption: Oggsoundfile

classDiagram
    class OggSoundFile {
        +prepareOgg()
        +read()
        +reset()
    }
```

```{mermaid}
:caption: Otmldocument

classDiagram
    class OTMLDocument {
        +create()
        +parse()
        +parseString()
        +parse()
        +emit()
        +save()
    }
```

```{mermaid}
:caption: Otmlemitter

classDiagram
    class OTMLEmitter {
        +emitNode()
    }
```

```{mermaid}
:caption: Otmlexception

classDiagram
    class OTMLException {
        #m_what
    }
```

```{mermaid}
:caption: Otmlnode

classDiagram
    class OTMLNode {
        +create()
        +create()
        +tag()
        +size()
        +source()
        +rawValue()
        +isUnique()
        +isNull()
        +hasTag()
        +hasValue()
        +hasChildren()
        +hasChildAt()
        +getIndex()
        +setTag()
        +setValue()
        +setNull()
        +setUnique()
        +setSource()
        +setIndex()
        +lockTag()
        ... (27 more members)
    }
```

```{mermaid}
:caption: Otmlparser

classDiagram
    class OTMLParser {
        +parse()
    }
```

```{mermaid}
:caption: Outfit

classDiagram
    class Outfit {
        +getColor()
        +draw()
        +draw()
        +setId()
        +setAuxId()
        +setHead()
        +setBody()
        +setLegs()
        +setFeet()
        +setAddons()
        +setMount()
        +setWings()
        +setAura()
        +setCategory()
        +setShader()
        +setHealthBar()
        +setManaBar()
        +setCenter()
        +resetClothes()
        +resetShader()
        ... (14 more members)
    }
    class DrawQueueItemOutfit {
    }
    class DrawQueueItemOutfitWithShader {
    }
```

```{mermaid}
:caption: Outputmessage

classDiagram
    class OutputMessage {
        +reset()
        +setBuffer()
        +getBuffer()
        +addU8()
        +addU16()
        +addU32()
        +addU64()
        +addString()
        +addRawString()
        +addPaddingBytes()
        +encryptRsa()
        +getWritePos()
        +getMessageSize()
        +setWritePos()
        +setMessageSize()
        #writeChecksum()
        #writeSequence()
        #writeMessageSize()
    }
```

```{mermaid}
:caption: Packed Any

classDiagram
    class can_pack_in_any {
    }
    class packed_any {
    }
    class placeholder {
    }
    class holder {
    }
```

```{mermaid}
:caption: Packed Storage

classDiagram
    class packed_storage {
    }
    class value_pair {
    }
```

```{mermaid}
:caption: Packet Player

classDiagram
    class PacketPlayer {
    }
```

```{mermaid}
:caption: Packet Recorder

classDiagram
    class PacketRecorder {
    }
```

```{mermaid}
:caption: Painter

classDiagram
    class Painter {
    }
    class PainterState {
    }
```

```{mermaid}
:caption: Paintershaderprogram

classDiagram
    class PainterShaderProgram {
    }
```

```{mermaid}
:caption: Platform

classDiagram
    class Platform {
        +processArgs()
        +spawnProcess()
        +getProcessId()
        +isProcessRunning()
        +killProcess()
        +getTempPath()
        +getCurrentDir()
        +copyFile()
        +fileExists()
        +removeFile()
        +getFileModificationTime()
        +openUrl()
        +openDir()
        +getCPUName()
        +getTotalSystemMemory()
        +getMemoryUsage()
        +getOSName()
        +traceback()
        +getMacAddresses()
        +getUserName()
        ... (3 more members)
    }
```

```{mermaid}
:caption: Platformwindow

classDiagram
    class PlatformWindow {
        +init()
        +terminate()
        +move()
        +resize()
        +show()
        +hide()
        +minimize()
        +maximize()
        +poll()
        +swapBuffers()
        +showMouse()
        +hideMouse()
        +displayFatalError()
        +loadMouseCursor()
        +setMouseCursor()
        +restoreMouseCursor()
        +setTitle()
        +setMinimumSize()
        +setFullscreen()
        +setVerticalSync()
        ... (58 more members)
    }
```

```{mermaid}
:caption: Player

classDiagram
    class Player {
        +asPlayer()
        +isPlayer()
    }
```

```{mermaid}
:caption: Pngunpacker

classDiagram
    class FileMetadata {
        +getOffset()
        +getFileSize()
    }
    class PngUnpacker {
        +unpack()
    }
```

```{mermaid}
:caption: Point

classDiagram
    class TSize {
        +isNull()
        +toSize()
        +operator
        +length()
        +manhattanLength()
        +distanceFrom()
    }
    class TPoint {
        +isNull()
        +toSize()
        +operator
        +length()
        +manhattanLength()
        +distanceFrom()
    }
```

```{mermaid}
:caption: Position

classDiagram
    class Position {
        +translatedToDirection()
        +pos
        +pos
        +translatedToReverseDirection()
        +pos
        +pos
        +translatedToDirections()
        +lastPos
        +positions
        +positions
        +positions
        +getAngleFromPositions()
        +dx
        +dy
        +angle
        +angle
        +getAngleFromPosition()
        +getAngleFromPositions()
        +angle
        +if()
        ... (37 more members)
    }
    class PositionHasher {
    }
```

```{mermaid}
:caption: Protocol

classDiagram
    class Protocol {
        +connect()
        +disconnect()
        +setRecorder()
        +playRecord()
        +isConnected()
        +isConnecting()
        +getElapsedTicksSinceLastRead()
        +getConnection()
        +setConnection()
        +generateXteaKey()
        +setXteaKey()
        +getXteaKey()
        +enableXteaEncryption()
        +enableChecksum()
        +enabledSequencedPackets()
        +enableBigPackets()
        +enableCompression()
        +send()
        +recv()
        +asProtocol()
        ... (11 more members)
    }
```

```{mermaid}
:caption: Protocolgame

classDiagram
    class ProtocolGame {
        +login()
        +send()
        +sendExtendedOpcode()
        +sendLoginPacket()
        +sendWorldName()
        +sendEnterGame()
        +sendLogout()
        +sendPing()
        +sendPingBack()
        +sendNewPing()
        +sendAutoWalk()
        +sendWalkNorth()
        +sendWalkEast()
        +sendWalkSouth()
        +sendWalkWest()
        +sendStop()
        +sendWalkNorthEast()
        +sendWalkSouthEast()
        +sendWalkSouthWest()
        +sendWalkNorthWest()
        ... (97 more members)
    }
```

```{mermaid}
:caption: Proxy

classDiagram
    class ProxyManager {
    }
```

```{mermaid}
:caption: Proxy Client

classDiagram
    class Session {
        +m_io()
        +start()
        +terminate()
        +getPing()
        +getRealPing()
        +getPriority()
        +isConnected()
        +getHost()
        +getPort()
        +getDebugInfo()
        +isActive()
        +addSession()
        +removeSession()
        +send()
    }
    class Proxy {
    }
    class Session {
    }
```

```{mermaid}
:caption: Qrcodegen

classDiagram
    class qrcodegen_Segment {
    }
    class qrcodegen_Segment {
    }
    class qrcodegen_Segment {
    }
    class qrcodegen_Segment {
    }
    class qrcodegen_Segment {
    }
```

```{mermaid}
:caption: Rect

classDiagram
    class TPoint {
        +isNull()
        +isEmpty()
        +isValid()
        +left()
        +top()
        +right()
        +bottom()
        +horizontalCenter()
        +verticalCenter()
        +x()
        +y()
        +topLeft()
        +bottomRight()
        +topRight()
        +bottomLeft()
        +topCenter()
        +bottomCenter()
        +centerLeft()
        +centerRight()
        +center()
        ... (102 more members)
    }
    class TSize {
        +isNull()
        +isEmpty()
        +isValid()
        +left()
        +top()
        +right()
        +bottom()
        +horizontalCenter()
        +verticalCenter()
        +x()
        +y()
        +topLeft()
        +bottomRight()
        +topRight()
        +bottomLeft()
        +topCenter()
        +bottomCenter()
        +centerLeft()
        +centerRight()
        +center()
        ... (102 more members)
    }
    class TRect {
        +isNull()
        +isEmpty()
        +isValid()
        +left()
        +top()
        +right()
        +bottom()
        +horizontalCenter()
        +verticalCenter()
        +x()
        +y()
        +topLeft()
        +bottomRight()
        +topRight()
        +bottomLeft()
        +topCenter()
        +bottomCenter()
        +centerLeft()
        +centerRight()
        +center()
        ... (102 more members)
    }
```

```{mermaid}
:caption: Resourcemanager

classDiagram
    class ResourceManager {
        +init()
        +terminate()
        +launchCorrect()
        +setupWriteDir()
        +setup()
        +getCompactName()
        +loadDataFromSelf()
        +fileExists()
        +directoryExists()
        +readFileStream()
        +readFileContents()
        +readFileContentsSafe()
        +isFileEncryptedOrCompressed()
        +writeFileBuffer()
        +writeFileContents()
        +writeFileStream()
        +openFile()
        +appendFile()
        +createFile()
        +deleteFile()
        ... (28 more members)
    }
```

```{mermaid}
:caption: Result

classDiagram
    class HttpSession {
    }
    class HttpResult {
    }
```

```{mermaid}
:caption: Scheduledevent

classDiagram
    class ScheduledEvent {
        +execute()
        +nextCycle()
        +ticks()
        +remainingTicks()
        +delay()
        +cyclesExecuted()
        +maxCycles()
    }
    class lessScheduledEvent {
    }
```

```{mermaid}
:caption: Sdlwindow

classDiagram
    class SDLWindow {
    }
```

```{mermaid}
:caption: Server

classDiagram
    class Server {
        +create()
        +isOpen()
        +close()
        +acceptNext()
    }
```

```{mermaid}
:caption: Session

classDiagram
    class HttpSession {
        +start()
        +cancel()
    }
```

```{mermaid}
:caption: Shader

classDiagram
    class Shader {
        +compileSourceCode()
        +compileSourceFile()
        +log()
        +getShaderId()
        +getShaderType()
    }
```

```{mermaid}
:caption: Shadermanager

classDiagram
    class ShaderManager {
        +init()
        +terminate()
        +createShader()
        +createOutfitShader()
        +createShader()
        +addTexture()
        +getShader()
    }
```

```{mermaid}
:caption: Shaderprogram

classDiagram
    class ShaderProgram {
    }
```

```{mermaid}
:caption: Shared Object

classDiagram
    class shared_object_ptr {
        +add_ref()
        +dec_ref()
        +ref_count()
    }
    class shared_object {
        +add_ref()
        +dec_ref()
        +ref_count()
    }
    class shared_object_ptr {
        +reset()
        +reset()
        +swap()
        +use_count()
        +is_unique()
        +unspecified_bool_type()
    }
```

```{mermaid}
:caption: Size

classDiagram
    class TSize {
        +toPoint()
        +isNull()
        +isEmpty()
        +isValid()
        +width()
        +height()
        +resize()
        +setWidth()
        +setHeight()
        +operator
        +expandedTo()
        +boundedTo()
        +scale()
        +useHeight
        +rw
        +scale()
        +ratio()
        +area()
    }
```

```{mermaid}
:caption: Soundbuffer

classDiagram
    class SoundBuffer {
        +fillBuffer()
        +fillBuffer()
        +getBufferId()
    }
```

```{mermaid}
:caption: Soundchannel

classDiagram
    class SoundChannel {
        +play()
        +stop()
        +enqueue()
        +enable()
        +disable()
        +setGain()
        +getGain()
        +setEnabled()
        +isEnabled()
        +getId()
        #update()
    }
    class QueueEntry {
    }
```

```{mermaid}
:caption: Soundfile

classDiagram
    class SoundFile {
        +loadSoundFile()
        +read()
        +reset()
        +eof()
        +getSampleFormat()
        +getChannels()
        +getRate()
        +getBps()
        +getSize()
        +getName()
        #m_file
        #m_channels
        #m_rate
        #m_bps
        #m_size
    }
```

```{mermaid}
:caption: Soundmanager

classDiagram
    class SoundManager {
        +init()
        +terminate()
        +poll()
        +setAudioEnabled()
        +isAudioEnabled()
        +enableAudio()
        +disableAudio()
        +stopAll()
        +preload()
        +play()
        +getChannel()
        +resolveSoundFile()
        +ensureContext()
    }
```

```{mermaid}
:caption: Soundsource

classDiagram
    class SoundSource {
        +play()
        +stop()
        +isBuffering()
        +isPlaying()
        +setName()
        +setLooping()
        +setRelative()
        +setReferenceDistance()
        +setGain()
        +setPitch()
        +setPosition()
        +setVelocity()
        +setFading()
        +getName()
        +getChannel()
        +getGain()
        #setBuffer()
        #setChannel()
        #update()
        #m_sourceId
        ... (8 more members)
    }
```

```{mermaid}
:caption: Spritemanager

classDiagram
    class SpriteManager {
        +terminate()
        +loadSpr()
        +unload()
        +saveSpr()
        +saveSpr64()
        +encryptSprites()
        +dumpSprites()
        +getSignature()
        +getSpritesCount()
        +getSpriteImage()
        +isLoaded()
        +spriteSize()
        +getOffsetFactor()
        +isHdMod()
    }
```

```{mermaid}
:caption: Statictext

classDiagram
    class StaticTextMessage {
    }
    class StaticText {
        +drawText()
        +getName()
        +getText()
        +getMessageMode()
        +getFirstMessage()
        +isYell()
        +setText()
        +setFont()
        +addMessage()
        +addColoredMessage()
        +asStaticText()
        +isStaticText()
        +setColor()
        +getColor()
        +hasText()
    }
```

```{mermaid}
:caption: Stats

classDiagram
    class Stat {
    }
    class StatsData {
    }
    class UIWidget {
        +add()
        +get()
        +clear()
        +clearAll()
        +getSlow()
        +clearSlow()
        +types()
        +getSleepTime()
        +m_sleepTime
        +resetSleepTime()
        +m_sleepTime
        +addWidget()
        +removeWidget()
        +getWidgetsInfo()
        +addTexture()
        +removeTexture()
        +addThing()
        +removeThing()
        +addCreature()
        +removeCreature()
    }
    class Stats {
    }
    class AutoStat {
    }
```

```{mermaid}
:caption: Streamsoundsource

classDiagram
    class StreamSoundSource {
        +play()
        +stop()
        +isPlaying()
        +setSoundFile()
        +downMix()
        +update()
    }
```

```{mermaid}
:caption: Textrender

classDiagram
    class TextRenderCache {
    }
    class TextRender {
        +init()
        +terminate()
        +poll()
        +addText()
        +drawText()
        +drawText()
        +drawColoredText()
    }
```

```{mermaid}
:caption: Texture

classDiagram
    class Texture {
        +replace()
        +resize()
        +update()
        +setUpsideDown()
        +setSmooth()
        +setRepeat()
        +buildHardwareMipmaps()
        +setTime()
        +setCanCache()
        +getId()
        +getUniqueId()
        +getTime()
        +getWidth()
        +getHeight()
        +isEmpty()
        +hasRepeat()
        +hasMipmaps()
        +canCache()
        +isAnimatedTexture()
        #uploadPixels()
        ... (18 more members)
    }
```

```{mermaid}
:caption: Texturemanager

classDiagram
    class TextureManager {
        +init()
        +terminate()
        +clearCache()
        +reload()
        +preload()
        +getTexture()
        +loadTexture()
    }
```

```{mermaid}
:caption: Thing

classDiagram
    class Thing {
        +draw()
        +setId()
        +setPosition()
        +getId()
        +getPosition()
        +getStackPriority()
        +getParentContainer()
        +getStackPos()
        +setMarked()
        +updatedMarkedColor()
        +isItem()
        +isEffect()
        +isMissile()
        +isCreature()
        +isNpc()
        +isMonster()
        +isPlayer()
        +isLocalPlayer()
        +isAnimatedText()
        +isStaticText()
        ... (73 more members)
    }
```

```{mermaid}
:caption: Thingstype

classDiagram
    class ThingsType {
        +load()
        +unload()
        +parseThingType()
        +getSignature()
        +isLoaded()
        +getFirstItemId()
        +getMaxItemid()
        +isValidItemId()
    }
```

```{mermaid}
:caption: Thingtype

classDiagram
    class MarketData {
    }
    class StoreCategory {
    }
    class StoreOffer {
    }
    class Imbuement {
    }
    class Light {
    }
    class DrawOutfitParams {
    }
    class ThingType {
        +unserialize()
        +unserializeOtml()
        +unload()
        +serialize()
        +exportImage()
        +replaceSprites()
        +drawOutfit()
        +getDrawSize()
        +drawWithShader()
        +drawWithShader()
        +getId()
        +getCategory()
        +isNull()
        +hasAttr()
        +isLoaded()
        +getLastUsage()
        +getSize()
        +getWidth()
        +getHeight()
        +getExactSize()
        ... (63 more members)
    }
    class DrawQueueItemThingWithShader {
    }
```

```{mermaid}
:caption: Thingtypemanager

classDiagram
    class ThingTypeManager {
        +init()
        +terminate()
        +check()
        +loadDat()
        +loadOtml()
        +loadOtb()
        +loadXml()
        +parseItemType()
        +saveDat()
        +dumpTextures()
        +replaceTextures()
        +addItemType()
        +findItemTypesByName()
        +findItemTypesByString()
        +getMarketCategories()
        +m_marketCategories
        +findThingTypeByAttr()
        +findItemTypeByCategory()
        +getDatSignature()
        +getOtbMajorVersion()
        ... (7 more members)
    }
```

```{mermaid}
:caption: Tile

classDiagram
    class Tile {
        +calculateCorpseCorrection()
        +drawGround()
        +drawBottom()
        +drawCreatures()
        +drawTop()
        +drawTexts()
        +drawWidget()
        +clean()
        +addWalkingCreature()
        +removeWalkingCreature()
        +addThing()
        +removeThing()
        +getThing()
        +getEffect()
        +hasThing()
        +getThingStackPos()
        +getTopThing()
        +getTopLookThing()
        +getTopLookThingEx()
        +getTopUseThing()
        ... (59 more members)
    }
```

```{mermaid}
:caption: Time

classDiagram
    class timer {
    }
```

```{mermaid}
:caption: Timer

classDiagram
    class Timer {
        +restart()
        +stop()
        +adjust()
        +startTicks()
        +ticksElapsed()
        +timeElapsed()
        +running()
    }
```

```{mermaid}
:caption: Tinystr

classDiagram
    class TiXmlString {
    }
    class Rep {
    }
    class TiXmlOutStream {
    }
```

```{mermaid}
:caption: Towns

classDiagram
    class Town {
        +setId()
        +setName()
        +setPos()
        +getId()
        +getName()
        +getPos()
    }
    class TownManager {
        +addTown()
        +removeTown()
        +sort()
        +getTowns()
        +clear()
        #findTown()
    }
```

```{mermaid}
:caption: Uianchorlayout

classDiagram
    class UIAnchor {
        +getAnchoredEdge()
        +getHookedEdge()
        +getHookedWidget()
        +getHookedPoint()
        #m_anchoredEdge
        #m_hookedEdge
        #m_hookedWidgetId
    }
    class UIAnchorGroup {
        +addAnchor()
        +isUpdated()
        +setUpdated()
    }
    class UIAnchorLayout {
        +removeAnchors()
        +hasAnchors()
        +centerIn()
        +fill()
        +addWidget()
        +removeWidget()
        +isUIAnchorLayout()
        #internalUpdate()
        #updateWidget()
        #m_anchorsGroups
    }
```

```{mermaid}
:caption: Uiboxlayout

classDiagram
    class UIBoxLayout {
        +applyStyle()
        +addWidget()
        +removeWidget()
        +setSpacing()
        +setFitChildren()
        +isUIBoxLayout()
        #m_fitChildren
        #m_spacing
    }
```

```{mermaid}
:caption: Uicreature

classDiagram
    class UICreature {
        +drawSelf()
        +setCreature()
        +setFixedCreatureSize()
        +setOutfit()
        +getCreature()
        +getOutfit()
        +isFixedCreatureSize()
        +setAutoRotating()
        +setDirection()
        +getDirection()
        +setScale()
        +getScale()
        +setAnimate()
        +isAnimating()
        +setCenter()
        +setOldScaling()
        #onStyleApply()
        #onGeometryChange()
        #m_creature
        #m_autoRotating
        ... (4 more members)
    }
```

```{mermaid}
:caption: Uigraph

classDiagram
    class UIGraph {
    }
```

```{mermaid}
:caption: Uigridlayout

classDiagram
    class UIGridLayout {
        +applyStyle()
        +removeWidget()
        +addWidget()
        +setCellSize()
        +setCellWidth()
        +setCellHeight()
        +setCellSpacing()
        +setNumColumns()
        +setNumLines()
        +setAutoSpacing()
        +setFitChildren()
        +setFlow()
        +getCellSize()
        +getCellSpacing()
        +getNumColumns()
        +getNumLines()
        +isUIGridLayout()
        #internalUpdate()
    }
```

```{mermaid}
:caption: Uihorizontallayout

classDiagram
    class UIHorizontalLayout {
        +applyStyle()
        +setAlignRight()
        +isUIHorizontalLayout()
        #internalUpdate()
        #m_alignChidren
        #m_alignRight
    }
```

```{mermaid}
:caption: Uiitem

classDiagram
    class UIItem {
        +drawSelf()
        +setItemId()
        +setItemCount()
        +setItemSubType()
        +setItemVisible()
        +setItem()
        +setVirtual()
        +clearItem()
        +setShowCount()
        +setItemShader()
        +getItemId()
        +getItemCount()
        +getItemSubType()
        +getItemCountOrSubType()
        +getItem()
        +isVirtual()
        +isItemVisible()
        #onStyleApply()
        #cacheCountText()
        #m_item
        ... (6 more members)
    }
```

```{mermaid}
:caption: Uilayout

classDiagram
    class UILayout {
        +update()
        +updateLater()
        +applyStyle()
        +addWidget()
        +removeWidget()
        +disableUpdates()
        +enableUpdates()
        +setParent()
        +getParentWidget()
        +isUpdateDisabled()
        +isUpdating()
        +isUIAnchorLayout()
        +isUIBoxLayout()
        +isUIHorizontalLayout()
        +isUIVerticalLayout()
        +isUIGridLayout()
        #internalUpdate()
        #m_updateDisabled
        #m_updating
        #m_updateScheduled
        ... (1 more members)
    }
```

```{mermaid}
:caption: Uimanager

classDiagram
    class UIManager {
        +init()
        +terminate()
        +render()
        +resize()
        +inputEvent()
        +updatePressedWidget()
        +updateDraggingWidget()
        +updateHoveredWidget()
        +clearStyles()
        +importStyle()
        +importStyleFromString()
        +importStyleFromOTML()
        +getStyle()
        +getStyleClass()
        +loadUIFromString()
        +loadUI()
        +displayUI()
        +createWidget()
        +createWidgetFromOTML()
        +setMouseReceiver()
        ... (16 more members)
    }
```

```{mermaid}
:caption: Uimap

classDiagram
    class UIMap {
        +onMouseMove()
        +drawSelf()
        +movePixels()
        +setZoom()
        +zoomIn()
        +zoomOut()
        +followCreature()
        +setCameraPosition()
        +setMaxZoomIn()
        +setMaxZoomOut()
        +setMultifloor()
        +lockVisibleFloor()
        +unlockVisibleFloor()
        +setVisibleDimension()
        +setDrawFlags()
        +setDrawTexts()
        +setDrawNames()
        +setDrawHealthBars()
        +setDrawHealthBarsOnTop()
        +setDrawLights()
        ... (34 more members)
    }
```

```{mermaid}
:caption: Uimapanchorlayout

classDiagram
    class UIPositionAnchor {
        +getHookedWidget()
        +getHookedPoint()
    }
    class UIMapAnchorLayout {
        +centerInPosition()
        +fillPosition()
    }
```

```{mermaid}
:caption: Uiminimap

classDiagram
    class UIMinimap {
        +drawSelf()
        +zoomIn()
        +zoomOut()
        +setZoom()
        +setMinZoom()
        +setMaxZoom()
        +setCameraPosition()
        +floorUp()
        +floorDown()
        +getTilePoint()
        +getTileRect()
        +getTilePosition()
        +getCameraPosition()
        +getMinZoom()
        +getMaxZoom()
        +getZoom()
        +getScale()
        +anchorPosition()
        +fillPosition()
        +centerInPosition()
        ... (3 more members)
    }
```

```{mermaid}
:caption: Uiprogressrect

classDiagram
    class UIProgressRect {
        +drawSelf()
        +setPercent()
        +getPercent()
        #onStyleApply()
        #m_percent
    }
```

```{mermaid}
:caption: Uisprite

classDiagram
    class UISprite {
        +drawSelf()
        +setSpriteId()
        +getSpriteId()
        +clearSprite()
        +setSpriteColor()
        +isSpriteVisible()
        +setSpriteVisible()
        +hasSprite()
        #onStyleApply()
        #m_sprite
        #m_spriteId
        #m_spriteColor
        #m_spriteVisible
    }
```

```{mermaid}
:caption: Uitextedit

classDiagram
    class UITextEdit {
        +drawSelf()
        +setCursorPos()
        +setSelection()
        +setCursorVisible()
        +setTextHidden()
        +setValidCharacters()
        +setShiftNavigation()
        +setMultiline()
        +setMaxLength()
        +setTextVirtualOffset()
        +setEditable()
        +setSelectable()
        +setSelectionColor()
        +setSelectionBackgroundColor()
        +setAutoScroll()
        +setAutoSubmit()
        +setPlaceholder()
        +setPlaceholderColor()
        +setPlaceholderAlign()
        +setPlaceholderFont()
        ... (44 more members)
    }
```

```{mermaid}
:caption: Uiverticallayout

classDiagram
    class UIVerticalLayout {
        +applyStyle()
        +setAlignBottom()
        +isAlignBottom()
        +isUIVerticalLayout()
        #internalUpdate()
        #m_alignBottom
    }
```

```{mermaid}
:caption: Uiwidget

classDiagram
    class EdgeGroup {
    }
    class UIWidget {
        +draw()
        #drawSelf()
        #drawChildren()
        #m_id
        #m_source
        #m_rect
        #m_virtualOffset
        #m_autoDraw
        #m_enabled
        #m_visible
        #m_focusable
        #m_fixedSize
        #m_phantom
        #m_draggable
        #m_destroyed
        #m_clipping
        #m_layout
        #m_parent
        #m_parentId
        #m_children
        ... (374 more members)
    }
```

```{mermaid}
:caption: Uri

classDiagram
    class ParsedURI {
    }
```

```{mermaid}
:caption: Vertexarray

classDiagram
    class VertexArray {
        +m_hardwareBuffer
        +addVertex()
        +addTriangle()
        +addRect()
        +top
        +right
        +bottom
        +left
        +addRect()
        +top
        +right
        +bottom
        +left
        +addQuad()
        +top
        +right
        +bottom
        +left
        +addUpsideDownQuad()
        +top
        ... (8 more members)
    }
```

```{mermaid}
:caption: Walkmatrix

classDiagram
    class WalkMatrix {
    }
```

```{mermaid}
:caption: Websocket

classDiagram
    class WebsocketSession {
        +start()
        +send()
        +close()
    }
```

```{mermaid}
:caption: Win32Window

classDiagram
    class WindowProcProxy {
        +init()
        +terminate()
        +move()
        +resize()
        +show()
        +hide()
        +minimize()
        +maximize()
        +poll()
        +swapBuffers()
        +showMouse()
        +hideMouse()
        +displayFatalError()
        +setMouseCursor()
        +restoreMouseCursor()
        +setTitle()
        +setMinimumSize()
        +setFullscreen()
        +setVerticalSync()
        +setIcon()
        ... (6 more members)
    }
    class WIN32Window {
        +init()
        +terminate()
        +move()
        +resize()
        +show()
        +hide()
        +minimize()
        +maximize()
        +poll()
        +swapBuffers()
        +showMouse()
        +hideMouse()
        +displayFatalError()
        +setMouseCursor()
        +restoreMouseCursor()
        +setTitle()
        +setMinimumSize()
        +setFullscreen()
        +setVerticalSync()
        +setIcon()
        ... (6 more members)
    }
```

```{mermaid}
:caption: X11Window

classDiagram
    class X11Window {
        +init()
        +terminate()
        +move()
        +resize()
        +show()
        +hide()
        +minimize()
        +maximize()
        +poll()
        +swapBuffers()
        +showMouse()
        +hideMouse()
        +setMouseCursor()
        +restoreMouseCursor()
        +setTitle()
        +setMinimumSize()
        +setFullscreen()
        +setVerticalSync()
        +setIcon()
        +setClipboardText()
        ... (5 more members)
    }
```


## Diagrams

```{mermaid}
:caption: Adaptiverenderer

classDiagram
    class AdaptiveRenderer {
    }
```

```{mermaid}
:caption: Android Native App Glue

classDiagram
    class android_app {
    }
    class android_poll_source {
    }
    class android_app {
    }
    class android_app {
    }
    class android_poll_source {
    }
    class android_poll_source {
    }
```

```{mermaid}
:caption: Androidwindow

classDiagram
    class AndroidWindow {
    }
```

```{mermaid}
:caption: Animatedtext

classDiagram
    class AnimatedText {
        +drawText()
        +setColor()
        +setText()
        +setOffset()
        +setFont()
        +getColor()
        +getOffset()
        +getTimer()
        +merge()
        +asAnimatedText()
        +isAnimatedText()
        +getText()
        #onAppear()
    }
```

```{mermaid}
:caption: Animatedtexture

classDiagram
    class AnimatedTexture {
        +replace()
        +update()
        +isAnimatedTexture()
        #buildHardwareMipmaps()
        #setSmooth()
        #setRepeat()
    }
```

```{mermaid}
:caption: Animator

classDiagram
    class Animator {
        +unserialize()
        +serialize()
        +setPhase()
        +getPhase()
        +getPhaseAt()
        +getStartPhase()
        +getAnimationPhases()
        +isAsync()
        +isComplete()
        +getTotalDuration()
        +resetAnimation()
    }
```

```{mermaid}
:caption: Any

classDiagram
    class any {
    }
    class placeholder {
    }
    class holder {
    }
```

```{mermaid}
:caption: Apngloader

classDiagram
    class apng_data {
    }
```

```{mermaid}
:caption: Application

classDiagram
    class Application {
        +init()
        +deinit()
        +terminate()
        +run()
        +poll()
        +exit()
        +quick_exit()
        +close()
        +restart()
        +restartArgs()
        +setName()
        +setCompactName()
        +setVersion()
        +isRunning()
        +isStopping()
        +isTerminated()
        +getCharset()
        +getBuildCompiler()
        +getBuildDate()
        +getBuildRevision()
        ... (19 more members)
    }
```

```{mermaid}
:caption: Asyncdispatcher

classDiagram
    class AsyncDispatcher {
    }
```

```{mermaid}
:caption: Atlas

classDiagram
    class Atlas {
    }
```

```{mermaid}
:caption: Binarytree

classDiagram
    class BinaryTree {
        +seek()
        +skip()
        +tell()
        +size()
        +getU8()
        +getU16()
        +getU32()
        +getU64()
        +getString()
        +getPoint()
        +getChildren()
        +canRead()
    }
    class OutputBinaryTree {
        +addU8()
        +addU16()
        +addU32()
        +addString()
        +addPos()
        +addPoint()
        +startNode()
        +endNode()
        #write()
    }
```

```{mermaid}
:caption: Bitmapfont

classDiagram
    class BitmapFont {
        +load()
        +drawText()
        +drawText()
        +drawColoredText()
        +calculateDrawTextCoords()
        +align
        +calculateTextRectSize()
        +wrapText()
        +getId()
        +getName()
        +getGlyphHeight()
        +getYOffset()
        +getGlyphSpacing()
    }
```

```{mermaid}
:caption: Boolean

classDiagram
    class boolean {
    }
```

```{mermaid}
:caption: Cachedtext

classDiagram
    class CachedText {
        +draw()
        +wrapText()
        +setFont()
        +setText()
        +setColoredText()
        +setAlign()
        +getTextSize()
        +getText()
        +getFont()
        +getAlign()
        +hasText()
    }
```

```{mermaid}
:caption: Cast

classDiagram
    class cast_exception {
    }
```

```{mermaid}
:caption: Client

classDiagram
    class Client {
        +init()
        +terminate()
        +registerLuaFunctions()
    }
```

```{mermaid}
:caption: Clock

classDiagram
    class Clock {
        +update()
        +micros()
        +millis()
        +seconds()
        +realMicros()
        +realMillis()
    }
```

```{mermaid}
:caption: Color

classDiagram
    class Color {
        +a()
        +b()
        +g()
        +r()
        +aF()
        +bF()
        +gF()
        +rF()
        +setRed()
        +setGreen()
        +setBlue()
        +setAlpha()
        +setRed()
        +setGreen()
        +setBlue()
        +setAlpha()
        +setRGBA()
        +setRGBA()
        +opacity()
        +Color()
        ... (14 more members)
    }
```

```{mermaid}
:caption: Colorarray

classDiagram
    class ColorArray {
        +addColor()
        +addColor()
        +clear()
        +colorCount()
        +count()
        +size()
    }
```

```{mermaid}
:caption: Combinedsoundsource

classDiagram
    class CombinedSoundSource {
        +addSource()
        +getSources()
        +play()
        +stop()
        +isBuffering()
        +isPlaying()
        +setLooping()
        +setRelative()
        +setReferenceDistance()
        +setGain()
        +setPitch()
        +setPosition()
        +setVelocity()
        +setFading()
        #update()
    }
```

```{mermaid}
:caption: Config

classDiagram
    class Config {
        +load()
        +unload()
        +save()
        +clear()
        +setValue()
        +setList()
        +getValue()
        +getList()
        +setNode()
        +mergeNode()
        +getNode()
        +getNodeSize()
        +exists()
        +remove()
        +getFileName()
        +isLoaded()
        +asConfig()
    }
```

```{mermaid}
:caption: Configmanager

classDiagram
    class ConfigManager {
        +init()
        +terminate()
        +getSettings()
        +get()
        +create()
        +loadSettings()
        +load()
        +unload()
        +remove()
        #m_settings
    }
```

```{mermaid}
:caption: Connection

classDiagram
    class Connection {
        +poll()
        +terminate()
        +connect()
        +close()
        +write()
        +read()
        +read_until()
        +read_some()
        +setErrorCallback()
        +getIp()
        +getError()
        +isConnecting()
        +isConnected()
        +getElapsedTicksSinceLastRead()
        +asConnection()
        #internal_connect()
        #internal_write()
        #onResolve()
        #onConnect()
        #onCanWrite()
        ... (18 more members)
    }
```

```{mermaid}
:caption: Consoleapplication

classDiagram
    class ConsoleApplication {
        +run()
    }
```

```{mermaid}
:caption: Container

classDiagram
    class Container {
        +getItem()
        +getItems()
        +getItemsCount()
        +getSlotPosition()
        +getId()
        +getCapacity()
        +getContainerItem()
        +getName()
        +hasParent()
        +isClosed()
        +isUnlocked()
        +hasPages()
        +getSize()
        +getFirstIndex()
        +findItemById()
        #onOpen()
        #onClose()
        #onAddItem()
        #onAddItems()
        #onUpdateItem()
        ... (1 more members)
    }
```

```{mermaid}
:caption: Coordsbuffer

classDiagram
    class CoordsBuffer {
        +clear()
        +addTriangle()
        +addRect()
        +addRect()
        +addRect()
        +addQuad()
        +addUpsideDownQuad()
        +addBoudingRect()
        +addRepeatedRects()
        +getVertexCount()
        +getTextureCoordCount()
        +unlock()
        +cache()
        +getTextureRect()
    }
```

```{mermaid}
:caption: Creature

classDiagram
    class Creature {
        +draw()
        +drawOutfit()
        +drawInformation()
        +isInsideOffset()
        +setId()
        +setName()
        +setManaPercent()
        +setHealthPercent()
        +setDirection()
        +setOutfit()
        +setOutfitColor()
        +setLight()
        +setSpeed()
        +setBaseSpeed()
        +setSkull()
        +setShield()
        +setEmblem()
        +setType()
        +setIcon()
        +setSkullTexture()
        ... (175 more members)
    }
    class Npc {
        +isNpc()
    }
    class Monster {
        +isMonster()
    }
```

```{mermaid}
:caption: Creatures

classDiagram
    class Spawn {
        +setRadius()
        +getRadius()
        +setCenterPos()
        +getCenterPos()
        +getCreatures()
        +addCreature()
        +removeCreature()
        +clear()
        #load()
        #save()
    }
    class CreatureType {
        +setSpawnTime()
        +getSpawnTime()
        +setName()
        +getName()
        +setOutfit()
        +getOutfit()
        +setDirection()
        +getDirection()
        +setRace()
        +getRace()
        +cast()
    }
    class CreatureManager {
        +clear()
        +clearSpawns()
        +terminate()
        +loadMonsters()
        +loadSingleCreature()
        +loadNpcs()
        +loadCreatureBuffer()
        +loadSpawns()
        +saveSpawns()
        +getSpawns()
        +getSpawn()
        +getSpawnForPlacePos()
        +addSpawn()
        +deleteSpawn()
        +isLoaded()
        +isSpawnLoaded()
        #internalLoadCreatureBuffer()
    }
```

```{mermaid}
:caption: Crypt

classDiagram
    class Crypt {
        +base64Encode()
        +base64Decode()
        +xorCrypt()
        +encrypt()
        +decrypt()
        +genUUID()
        +setMachineUUID()
        +getMachineUUID()
        +md5Encode()
        +sha1Encode()
        +sha256Encode()
        +sha512Encode()
        +crc32()
        +rsaGenerateKey()
        +rsaSetPublicKey()
        +rsaSetPrivateKey()
        +rsaCheckKey()
        +rsaEncrypt()
        +rsaDecrypt()
        +rsaGetSize()
        ... (2 more members)
    }
```

```{mermaid}
:caption: Databuffer

classDiagram
    class DataBuffer {
        +reset()
        +clear()
        +empty()
        +size()
        +reserve()
        +resize()
        +grow()
        +newcapacity
        +add()
    }
```

```{mermaid}
:caption: Declarations

classDiagram
    class UIManager {
    }
    class UIWidget {
    }
    class UITextEdit {
    }
    class UILayout {
    }
    class UIBoxLayout {
    }
    class UIHorizontalLayout {
    }
    class UIVerticalLayout {
    }
    class UIGridLayout {
    }
    class UIAnchor {
    }
    class UIAnchorGroup {
    }
    class UIAnchorLayout {
    }
```

```{mermaid}
:caption: Deptharray

classDiagram
    class DepthArray {
        +addDepth()
        +clear()
        +depthCount()
        +count()
        +size()
    }
```

```{mermaid}
:caption: Drawcache

classDiagram
    class DrawCache {
    }
```

```{mermaid}
:caption: Drawqueue

classDiagram
    class DrawQueue {
    }
    class DrawQueueItem {
    }
    class DrawQueueItem {
    }
    class DrawQueueItemTexturedRect {
    }
    class DrawQueueItemTextureCoords {
    }
    class DrawQueueItemColoredTextureCoords {
    }
    class DrawQueueItemImageWithShader {
    }
    class DrawQueueItemFilledRect {
    }
    class DrawQueueItemClearRect {
    }
    class DrawQueueItemFillCoords {
    }
    class DrawQueueItemText {
    }
    class DrawQueueItemTextColored {
    }
    class DrawQueueItemLine {
    }
    class DrawQueueCondition {
    }
    class DrawQueueConditionClip {
    }
    class DrawQueueConditionRotation {
    }
    class DrawQueueConditionMark {
    }
    class DrawQueue {
    }
```

```{mermaid}
:caption: Dumper

classDiagram
    class dumper_dummy {
    }
```

```{mermaid}
:caption: Dynamic Storage

classDiagram
    class dynamic_storage {
    }
```

```{mermaid}
:caption: Effect

classDiagram
    class Effect {
        +draw()
        +draw()
        +setId()
        +getId()
        +asEffect()
        +isEffect()
        #onAppear()
    }
```

```{mermaid}
:caption: Event

classDiagram
    class Event {
        +execute()
        +cancel()
        +isCanceled()
        +isExecuted()
        +isBotSafe()
        #m_function
        #m_callback
        #m_canceled
        #m_executed
        #m_botSafe
    }
```

```{mermaid}
:caption: Eventdispatcher

classDiagram
    class EventDispatcher {
        +shutdown()
        +poll()
        +addEventEx()
        +scheduleEventEx()
        +cycleEventEx()
        +isBotSafe()
    }
```

```{mermaid}
:caption: Exception

classDiagram
    class exception {
        #m_what
    }
```

```{mermaid}
:caption: Extras

classDiagram
    class Extras {
    }
```

```{mermaid}
:caption: Filestream

classDiagram
    class PHYSFS_File {
        +close()
        +flush()
        +write()
        +read()
        +seek()
        +skip()
        +size()
        +tell()
        +eof()
        +name()
        +getU8()
        +getU16()
        +getU32()
        +getU64()
        +get8()
        +get16()
        +get32()
        +get64()
        +getString()
        +getBinaryTree()
        ... (14 more members)
    }
    class FileStream {
        +close()
        +flush()
        +write()
        +read()
        +seek()
        +skip()
        +size()
        +tell()
        +eof()
        +name()
        +getU8()
        +getU16()
        +getU32()
        +getU64()
        +get8()
        +get16()
        +get32()
        +get64()
        +getString()
        +getBinaryTree()
        ... (14 more members)
    }
```

```{mermaid}
:caption: Fontmanager

classDiagram
    class FontManager {
        +terminate()
        +clearFonts()
        +importFont()
        +fontExists()
        +getFont()
        +getDefaultFont()
        +setDefaultFont()
    }
```

```{mermaid}
:caption: Framebuffer

classDiagram
    class FrameBuffer {
        +resize()
        +bind()
        +release()
        +draw()
        +draw()
        +draw()
        +setSmooth()
        +getTexture()
        +getSize()
        +isSmooth()
        +getDepthRenderBuffer()
        +hasDepth()
        +readPixels()
        +doScreenshot()
    }
```

```{mermaid}
:caption: Framebuffermanager

classDiagram
    class FrameBufferManager {
        +init()
        +terminate()
        +clear()
        +createFrameBuffer()
        #m_temporaryFramebuffer
        #m_drawQueueTemporaryFramebuffer
        #m_framebuffers
    }
```

```{mermaid}
:caption: Framecounter

classDiagram
    class FrameCounter {
    }
```

```{mermaid}
:caption: Game

classDiagram
    class UnjustifiedPoints {
    }
    class Game {
        +init()
        +terminate()
        #processConnectionError()
        #processDisconnect()
        #processPing()
        #processPingBack()
        #processNewPing()
        #processUpdateNeeded()
        #processLoginError()
        #processLoginAdvice()
        #processLoginWait()
        #processLoginToken()
        #processLogin()
        #processPendingGame()
        #processEnterGame()
        #processGameStart()
        #processGameEnd()
        #processDeath()
        #processGMActions()
        #processInventoryChange()
        ... (205 more members)
    }
```

```{mermaid}
:caption: Graph

classDiagram
    class Graph {
        +draw()
        +clear()
        +addValue()
    }
```

```{mermaid}
:caption: Graphicalapplication

classDiagram
    class GraphicalApplication {
        +init()
        +deinit()
        +terminate()
        +run()
        +poll()
        +pollGraphics()
        +close()
        +willRepaint()
        +repaint()
        +setMaxFps()
        +getMaxFps()
        +getFps()
        +getGraphicsFps()
        +getProcessingFps()
        +isOnInputEvent()
        +getIteration()
        +m_iteration
        +doScreenshot()
        +scaleUp()
        +scaleDown()
        ... (5 more members)
    }
```

```{mermaid}
:caption: Graphics

classDiagram
    class Painter {
        +init()
        +terminate()
        +resize()
        +checkDepthSupport()
        +getMaxTextureSize()
        +getVendor()
        +getRenderer()
        +getVersion()
        +getExtensions()
        +ok()
        +checkForError()
    }
    class Graphics {
        +init()
        +terminate()
        +resize()
        +checkDepthSupport()
        +getMaxTextureSize()
        +getVendor()
        +getRenderer()
        +getVersion()
        +getExtensions()
        +ok()
        +checkForError()
    }
```

```{mermaid}
:caption: Hardwarebuffer

classDiagram
    class HardwareBuffer {
        +bind()
        +unbind()
        +write()
    }
```

```{mermaid}
:caption: Healthbars

classDiagram
    class HealthBar {
        +setPath()
        +getPath()
        +setTexture()
        +getTexture()
        +setOffset()
        +getOffset()
        +setBarOffset()
        +getBarOffset()
        +setHeight()
        +getHeight()
    }
    class HealthBars {
        +init()
        +terminate()
        +addHealthBackground()
        +addManaBackground()
        +getHealthBar()
        +getManaBar()
        +getHealthBarPath()
        +getManaBarPath()
        +getHealthBarOffset()
        +getManaBarOffset()
        +getHealthBarOffsetBar()
        +getManaBarOffsetBar()
        +getHealthBarHeight()
        +getManaBarHeight()
    }
```

```{mermaid}
:caption: Houses

classDiagram
    class House {
        +setTile()
        +getTile()
        +setName()
        +getName()
        +setId()
        +getId()
        +setTownId()
        +getTownId()
        +setSize()
        +getSize()
        +setRent()
        +getRent()
        +setEntry()
        +getEntry()
        +addDoor()
        +removeDoor()
        +removeDoorById()
        #load()
        #save()
    }
    class HouseManager {
    }
```

```{mermaid}
:caption: Http

classDiagram
    class WebsocketSession {
        +init()
        +terminate()
        +get()
        +post()
        +download()
        +ws()
        +wsSend()
        +wsClose()
        +cancel()
        +m_downloads
        +clearDownloads()
        +getFile()
        +it
        +nullptr
        +setUserAgent()
    }
    class Http {
    }
```

```{mermaid}
:caption: Image

classDiagram
    class Image {
        +load()
        +loadPNG()
        +loadPNG()
        +savePNG()
        +blit()
        +paste()
        +upscale()
        +resize()
        +nextMipmap()
        +setPixel()
        +setPixel()
        +setPixel()
        +getPixelCount()
        +getWidth()
        +getHeight()
        +getBpp()
        +fromQRCode()
    }
```

```{mermaid}
:caption: Inputevent

classDiagram
    class InputEvent {
    }
```

```{mermaid}
:caption: Inputmessage

classDiagram
    class InputMessage {
        +setBuffer()
        +getBuffer()
        +getBodyBuffer()
        +skipBytes()
        +setReadPos()
        +getU8()
        +getU16()
        +getU32()
        +getU64()
        +getString()
        +getDouble()
        +peekU8()
        +peekU16()
        +peekU32()
        +peekU64()
        +decryptRsa()
        +getHeaderPos()
        +getHeaderSize()
        +getReadSize()
        +getReadPos()
        ... (10 more members)
    }
```

```{mermaid}
:caption: Item

classDiagram
    class Item {
        +create()
        +createFromOtb()
        +draw()
        +draw()
        +setId()
        +setOtbId()
        +setCountOrSubType()
        +setCount()
        +setSubType()
        +setColor()
        +setTooltip()
        +setQuickLootFlags()
        +setShader()
        +getCountOrSubType()
        +getSubType()
        +getCount()
        +getId()
        +getClientId()
        +getServerId()
        +getName()
        ... (42 more members)
    }
```

```{mermaid}
:caption: Itemtype

classDiagram
    class ItemType {
        +unserialize()
        +setServerId()
        +getServerId()
        +setClientId()
        +getClientId()
        +setCategory()
        +getCategory()
        +setName()
        +getName()
        +setDesc()
        +getDesc()
        +isNull()
        +isWritable()
    }
```

```{mermaid}
:caption: Lbitlib

classDiagram
    class lua_State {
    }
```

```{mermaid}
:caption: Lightview

classDiagram
    class TileLight {
    }
    class LightView {
        +addLight()
        +addLight()
        +addLight()
        +setFieldBrightness()
        +size()
        +draw()
    }
```

```{mermaid}
:caption: Localplayer

classDiagram
    class LocalPlayer {
        +draw()
        +unlockWalk()
        +lockWalk()
        +stopAutoWalk()
        +autoWalk()
        +canWalk()
        +isWalkLocked()
        +turn()
        +setStates()
        +setSkill()
        +setBaseSkill()
        +setHealth()
        +setFreeCapacity()
        +setTotalCapacity()
        +setExperience()
        +setLevel()
        +setMana()
        +setMagicLevel()
        +setBaseMagicLevel()
        +setSoul()
        ... (64 more members)
    }
```

```{mermaid}
:caption: Logger

classDiagram
    class LogMessage {
    }
    class Logger {
        +log()
        +logFunc()
        +debug()
        +info()
        +warning()
        +error()
        +fatal()
        +fireOldMessages()
        +setLogFile()
        +setOnLog()
        +getLastLog()
        +m_lastLog
        +setTestingMode()
    }
```

```{mermaid}
:caption: Luabinder

classDiagram
    class pack_values_into_tuple {
    }
    class pack_values_into_tuple {
    }
    class expand_fun_arguments {
    }
    class expand_fun_arguments {
    }
    class bind_lambda_fun {
    }
    class bind_lambda_fun {
    }
```

```{mermaid}
:caption: Luaexception

classDiagram
    class LuaException {
        +generateLuaErrorMessage()
        #m_what
    }
    class LuaBadNumberOfArgumentsException {
    }
    class LuaBadValueCastException {
    }
```

```{mermaid}
:caption: Luainterface

classDiagram
    class lua_State {
        +init()
        +terminate()
        +registerFunctions()
        +registerSingletonClass()
        +registerClass()
        +registerClass()
        +registerClassStaticFunction()
        +registerClassMemberFunction()
        +bindSingletonFunction()
        +bindSingletonFunction()
        +bindSingletonFunction()
        +bindClassStaticFunction()
        +bindClassStaticFunction()
        +bindClassMemberFunction()
        +bindClassMemberFunction()
        +bindClassMemberField()
        +bindClassMemberField()
        +bindClassMemberGetField()
        +bindClassMemberGetField()
        +bindClassMemberSetField()
        ... (105 more members)
    }
    class LuaInterface {
        +init()
        +terminate()
        +registerFunctions()
        +registerSingletonClass()
        +registerClass()
        +registerClass()
        +registerClassStaticFunction()
        +registerClassMemberFunction()
        +bindSingletonFunction()
        +bindSingletonFunction()
        +bindSingletonFunction()
        +bindClassStaticFunction()
        +bindClassStaticFunction()
        +bindClassMemberFunction()
        +bindClassMemberFunction()
        +bindClassMemberField()
        +bindClassMemberField()
        +bindClassMemberGetField()
        +bindClassMemberGetField()
        +bindClassMemberSetField()
        ... (105 more members)
    }
```

```{mermaid}
:caption: Luaobject

classDiagram
    class LuaObject {
        +connectLuaField()
        +luaCallLuaField()
        +callLuaField()
        +callLuaField()
        +hasLuaField()
        +setLuaField()
        +getLuaField()
        +releaseLuaFieldsTable()
        +luaSetField()
        +luaGetField()
        +luaGetMetatable()
        +luaGetFieldsTable()
        +getUseCount()
        +getClassName()
        +asLuaObject()
        +operator
    }
    class connect_lambda {
    }
    class connect_lambda {
    }
```

```{mermaid}
:caption: Luavaluecasts

classDiagram
    class push_tuple_internal_luavalue {
    }
    class push_tuple_internal_luavalue {
    }
    class push_tuple_luavalue {
    }
    class push_tuple_luavalue {
    }
```

```{mermaid}
:caption: Map

classDiagram
    class TileBlock {
    }
    class AwareRange {
    }
    class PathFindResult {
    }
    class Node {
    }
    class Map {
        +init()
        +terminate()
        +addMapView()
        +removeMapView()
        +notificateTileUpdate()
        +requestVisibleTilesCacheUpdate()
        +loadOtcm()
        +saveOtcm()
        +loadOtbm()
        +saveOtbm()
        +setHouseFile()
        +setSpawnFile()
        +setDescription()
        +clearDescriptions()
        +setWidth()
        +setHeight()
        +getHouseFile()
        +getSpawnFile()
        +getSize()
        +getDescriptions()
        ... (58 more members)
    }
```

```{mermaid}
:caption: Mapview

classDiagram
    class MapView {
        +drawMapBackground()
        +drawMapForeground()
        #onTileUpdate()
        #onMapCenterChange()
        +lockFirstVisibleFloor()
        +unlockFirstVisibleFloor()
        +getLockedFirstVisibleFloor()
        +setMultifloor()
        +isMultifloor()
        +setVisibleDimension()
        +optimizeForSize()
        +getVisibleDimension()
        +getVisibleCenterOffset()
        +getCachedFirstVisibleFloor()
        +getCachedLastVisibleFloor()
        +followCreature()
        +getFollowingCreature()
        +isFollowingCreature()
        +setCameraPosition()
        +getCameraPosition()
        ... (25 more members)
    }
```

```{mermaid}
:caption: Matrix

classDiagram
    class Matrix {
        +setIdentity()
        +isIdentity()
        +fill()
        +transposed()
        +operator()
        +operator
    }
```

```{mermaid}
:caption: Minimap

classDiagram
    class MinimapTile {
    }
    class MinimapBlock {
        +clean()
        +update()
        +updateTile()
        +resetTile()
        +getTileIndex()
        +mustUpdate()
        +justSaw()
        +wasSeen()
    }
    class Minimap {
        +init()
        +terminate()
        +clean()
        +draw()
        +getTilePoint()
        +getTilePosition()
        +getTileRect()
        +updateTile()
        +threadGetTile()
        +loadImage()
        +saveImage()
        +loadOtmm()
        +saveOtmm()
    }
```

```{mermaid}
:caption: Missile

classDiagram
    class Missile {
        +draw()
        +setId()
        +setPath()
        +getId()
        +asMissile()
        +isMissile()
        +getSource()
        +getDestination()
    }
```

```{mermaid}
:caption: Module

classDiagram
    class Module {
        +load()
        +unload()
        +reload()
        +canUnload()
        +canReload()
        +isLoaded()
        +isReloadable()
        +isDependent()
        +isSandboxed()
        +hasDependency()
        +getSandbox()
        +getDescription()
        +getName()
        +getAuthor()
        +getWebsite()
        +getVersion()
        +isAutoLoad()
        +getAutoLoadPriority()
        +asModule()
        #discover()
    }
```

```{mermaid}
:caption: Modulemanager

classDiagram
    class ModuleManager {
        +clear()
        +discoverModules()
        +autoLoadModules()
        +discoverModule()
        +ensureModuleLoaded()
        +unloadModules()
        +reloadModules()
        +getModule()
        +getModules()
        #updateModuleLoadOrder()
    }
```

```{mermaid}
:caption: Mouse

classDiagram
    class Mouse {
        +init()
        +terminate()
        +loadCursors()
        +addCursor()
        +pushCursor()
        +popCursor()
        +isCursorChanged()
        +isPressed()
    }
```

```{mermaid}
:caption: Oggsoundfile

classDiagram
    class OggSoundFile {
        +prepareOgg()
        +read()
        +reset()
    }
```

```{mermaid}
:caption: Otmldocument

classDiagram
    class OTMLDocument {
        +create()
        +parse()
        +parseString()
        +parse()
        +emit()
        +save()
    }
```

```{mermaid}
:caption: Otmlemitter

classDiagram
    class OTMLEmitter {
        +emitNode()
    }
```

```{mermaid}
:caption: Otmlexception

classDiagram
    class OTMLException {
        #m_what
    }
```

```{mermaid}
:caption: Otmlnode

classDiagram
    class OTMLNode {
        +create()
        +create()
        +tag()
        +size()
        +source()
        +rawValue()
        +isUnique()
        +isNull()
        +hasTag()
        +hasValue()
        +hasChildren()
        +hasChildAt()
        +getIndex()
        +setTag()
        +setValue()
        +setNull()
        +setUnique()
        +setSource()
        +setIndex()
        +lockTag()
        ... (27 more members)
    }
```

```{mermaid}
:caption: Otmlparser

classDiagram
    class OTMLParser {
        +parse()
    }
```

```{mermaid}
:caption: Outfit

classDiagram
    class Outfit {
        +getColor()
        +draw()
        +draw()
        +setId()
        +setAuxId()
        +setHead()
        +setBody()
        +setLegs()
        +setFeet()
        +setAddons()
        +setMount()
        +setWings()
        +setAura()
        +setCategory()
        +setShader()
        +setHealthBar()
        +setManaBar()
        +setCenter()
        +resetClothes()
        +resetShader()
        ... (14 more members)
    }
    class DrawQueueItemOutfit {
    }
    class DrawQueueItemOutfitWithShader {
    }
```

```{mermaid}
:caption: Outputmessage

classDiagram
    class OutputMessage {
        +reset()
        +setBuffer()
        +getBuffer()
        +addU8()
        +addU16()
        +addU32()
        +addU64()
        +addString()
        +addRawString()
        +addPaddingBytes()
        +encryptRsa()
        +getWritePos()
        +getMessageSize()
        +setWritePos()
        +setMessageSize()
        #writeChecksum()
        #writeSequence()
        #writeMessageSize()
    }
```

```{mermaid}
:caption: Packed Any

classDiagram
    class can_pack_in_any {
    }
    class packed_any {
    }
    class placeholder {
    }
    class holder {
    }
```

```{mermaid}
:caption: Packed Storage

classDiagram
    class packed_storage {
    }
    class value_pair {
    }
```

```{mermaid}
:caption: Packet Player

classDiagram
    class PacketPlayer {
    }
```

```{mermaid}
:caption: Packet Recorder

classDiagram
    class PacketRecorder {
    }
```

```{mermaid}
:caption: Painter

classDiagram
    class Painter {
    }
    class PainterState {
    }
```

```{mermaid}
:caption: Paintershaderprogram

classDiagram
    class PainterShaderProgram {
    }
```

```{mermaid}
:caption: Platform

classDiagram
    class Platform {
        +processArgs()
        +spawnProcess()
        +getProcessId()
        +isProcessRunning()
        +killProcess()
        +getTempPath()
        +getCurrentDir()
        +copyFile()
        +fileExists()
        +removeFile()
        +getFileModificationTime()
        +openUrl()
        +openDir()
        +getCPUName()
        +getTotalSystemMemory()
        +getMemoryUsage()
        +getOSName()
        +traceback()
        +getMacAddresses()
        +getUserName()
        ... (3 more members)
    }
```

```{mermaid}
:caption: Platformwindow

classDiagram
    class PlatformWindow {
        +init()
        +terminate()
        +move()
        +resize()
        +show()
        +hide()
        +minimize()
        +maximize()
        +poll()
        +swapBuffers()
        +showMouse()
        +hideMouse()
        +displayFatalError()
        +loadMouseCursor()
        +setMouseCursor()
        +restoreMouseCursor()
        +setTitle()
        +setMinimumSize()
        +setFullscreen()
        +setVerticalSync()
        ... (58 more members)
    }
```

```{mermaid}
:caption: Player

classDiagram
    class Player {
        +asPlayer()
        +isPlayer()
    }
```

```{mermaid}
:caption: Pngunpacker

classDiagram
    class FileMetadata {
        +getOffset()
        +getFileSize()
    }
    class PngUnpacker {
        +unpack()
    }
```

```{mermaid}
:caption: Point

classDiagram
    class TSize {
        +isNull()
        +toSize()
        +operator
        +length()
        +manhattanLength()
        +distanceFrom()
    }
    class TPoint {
        +isNull()
        +toSize()
        +operator
        +length()
        +manhattanLength()
        +distanceFrom()
    }
```

```{mermaid}
:caption: Position

classDiagram
    class Position {
        +translatedToDirection()
        +pos
        +pos
        +translatedToReverseDirection()
        +pos
        +pos
        +translatedToDirections()
        +lastPos
        +positions
        +positions
        +positions
        +getAngleFromPositions()
        +dx
        +dy
        +angle
        +angle
        +getAngleFromPosition()
        +getAngleFromPositions()
        +angle
        +if()
        ... (37 more members)
    }
    class PositionHasher {
    }
```

```{mermaid}
:caption: Protocol

classDiagram
    class Protocol {
        +connect()
        +disconnect()
        +setRecorder()
        +playRecord()
        +isConnected()
        +isConnecting()
        +getElapsedTicksSinceLastRead()
        +getConnection()
        +setConnection()
        +generateXteaKey()
        +setXteaKey()
        +getXteaKey()
        +enableXteaEncryption()
        +enableChecksum()
        +enabledSequencedPackets()
        +enableBigPackets()
        +enableCompression()
        +send()
        +recv()
        +asProtocol()
        ... (11 more members)
    }
```

```{mermaid}
:caption: Protocolgame

classDiagram
    class ProtocolGame {
        +login()
        +send()
        +sendExtendedOpcode()
        +sendLoginPacket()
        +sendWorldName()
        +sendEnterGame()
        +sendLogout()
        +sendPing()
        +sendPingBack()
        +sendNewPing()
        +sendAutoWalk()
        +sendWalkNorth()
        +sendWalkEast()
        +sendWalkSouth()
        +sendWalkWest()
        +sendStop()
        +sendWalkNorthEast()
        +sendWalkSouthEast()
        +sendWalkSouthWest()
        +sendWalkNorthWest()
        ... (97 more members)
    }
```

```{mermaid}
:caption: Proxy

classDiagram
    class ProxyManager {
    }
```

```{mermaid}
:caption: Proxy Client

classDiagram
    class Session {
        +m_io()
        +start()
        +terminate()
        +getPing()
        +getRealPing()
        +getPriority()
        +isConnected()
        +getHost()
        +getPort()
        +getDebugInfo()
        +isActive()
        +addSession()
        +removeSession()
        +send()
    }
    class Proxy {
    }
    class Session {
    }
```

```{mermaid}
:caption: Qrcodegen

classDiagram
    class qrcodegen_Segment {
    }
    class qrcodegen_Segment {
    }
    class qrcodegen_Segment {
    }
    class qrcodegen_Segment {
    }
    class qrcodegen_Segment {
    }
```

```{mermaid}
:caption: Rect

classDiagram
    class TPoint {
        +isNull()
        +isEmpty()
        +isValid()
        +left()
        +top()
        +right()
        +bottom()
        +horizontalCenter()
        +verticalCenter()
        +x()
        +y()
        +topLeft()
        +bottomRight()
        +topRight()
        +bottomLeft()
        +topCenter()
        +bottomCenter()
        +centerLeft()
        +centerRight()
        +center()
        ... (102 more members)
    }
    class TSize {
        +isNull()
        +isEmpty()
        +isValid()
        +left()
        +top()
        +right()
        +bottom()
        +horizontalCenter()
        +verticalCenter()
        +x()
        +y()
        +topLeft()
        +bottomRight()
        +topRight()
        +bottomLeft()
        +topCenter()
        +bottomCenter()
        +centerLeft()
        +centerRight()
        +center()
        ... (102 more members)
    }
    class TRect {
        +isNull()
        +isEmpty()
        +isValid()
        +left()
        +top()
        +right()
        +bottom()
        +horizontalCenter()
        +verticalCenter()
        +x()
        +y()
        +topLeft()
        +bottomRight()
        +topRight()
        +bottomLeft()
        +topCenter()
        +bottomCenter()
        +centerLeft()
        +centerRight()
        +center()
        ... (102 more members)
    }
```

```{mermaid}
:caption: Resourcemanager

classDiagram
    class ResourceManager {
        +init()
        +terminate()
        +launchCorrect()
        +setupWriteDir()
        +setup()
        +getCompactName()
        +loadDataFromSelf()
        +fileExists()
        +directoryExists()
        +readFileStream()
        +readFileContents()
        +readFileContentsSafe()
        +isFileEncryptedOrCompressed()
        +writeFileBuffer()
        +writeFileContents()
        +writeFileStream()
        +openFile()
        +appendFile()
        +createFile()
        +deleteFile()
        ... (28 more members)
    }
```

```{mermaid}
:caption: Result

classDiagram
    class HttpSession {
    }
    class HttpResult {
    }
```

```{mermaid}
:caption: Scheduledevent

classDiagram
    class ScheduledEvent {
        +execute()
        +nextCycle()
        +ticks()
        +remainingTicks()
        +delay()
        +cyclesExecuted()
        +maxCycles()
    }
    class lessScheduledEvent {
    }
```

```{mermaid}
:caption: Sdlwindow

classDiagram
    class SDLWindow {
    }
```

```{mermaid}
:caption: Server

classDiagram
    class Server {
        +create()
        +isOpen()
        +close()
        +acceptNext()
    }
```

```{mermaid}
:caption: Session

classDiagram
    class HttpSession {
        +start()
        +cancel()
    }
```

```{mermaid}
:caption: Shader

classDiagram
    class Shader {
        +compileSourceCode()
        +compileSourceFile()
        +log()
        +getShaderId()
        +getShaderType()
    }
```

```{mermaid}
:caption: Shadermanager

classDiagram
    class ShaderManager {
        +init()
        +terminate()
        +createShader()
        +createOutfitShader()
        +createShader()
        +addTexture()
        +getShader()
    }
```

```{mermaid}
:caption: Shaderprogram

classDiagram
    class ShaderProgram {
    }
```

```{mermaid}
:caption: Shared Object

classDiagram
    class shared_object_ptr {
        +add_ref()
        +dec_ref()
        +ref_count()
    }
    class shared_object {
        +add_ref()
        +dec_ref()
        +ref_count()
    }
    class shared_object_ptr {
        +reset()
        +reset()
        +swap()
        +use_count()
        +is_unique()
        +unspecified_bool_type()
    }
```

```{mermaid}
:caption: Size

classDiagram
    class TSize {
        +toPoint()
        +isNull()
        +isEmpty()
        +isValid()
        +width()
        +height()
        +resize()
        +setWidth()
        +setHeight()
        +operator
        +expandedTo()
        +boundedTo()
        +scale()
        +useHeight
        +rw
        +scale()
        +ratio()
        +area()
    }
```

```{mermaid}
:caption: Soundbuffer

classDiagram
    class SoundBuffer {
        +fillBuffer()
        +fillBuffer()
        +getBufferId()
    }
```

```{mermaid}
:caption: Soundchannel

classDiagram
    class SoundChannel {
        +play()
        +stop()
        +enqueue()
        +enable()
        +disable()
        +setGain()
        +getGain()
        +setEnabled()
        +isEnabled()
        +getId()
        #update()
    }
    class QueueEntry {
    }
```

```{mermaid}
:caption: Soundfile

classDiagram
    class SoundFile {
        +loadSoundFile()
        +read()
        +reset()
        +eof()
        +getSampleFormat()
        +getChannels()
        +getRate()
        +getBps()
        +getSize()
        +getName()
        #m_file
        #m_channels
        #m_rate
        #m_bps
        #m_size
    }
```

```{mermaid}
:caption: Soundmanager

classDiagram
    class SoundManager {
        +init()
        +terminate()
        +poll()
        +setAudioEnabled()
        +isAudioEnabled()
        +enableAudio()
        +disableAudio()
        +stopAll()
        +preload()
        +play()
        +getChannel()
        +resolveSoundFile()
        +ensureContext()
    }
```

```{mermaid}
:caption: Soundsource

classDiagram
    class SoundSource {
        +play()
        +stop()
        +isBuffering()
        +isPlaying()
        +setName()
        +setLooping()
        +setRelative()
        +setReferenceDistance()
        +setGain()
        +setPitch()
        +setPosition()
        +setVelocity()
        +setFading()
        +getName()
        +getChannel()
        +getGain()
        #setBuffer()
        #setChannel()
        #update()
        #m_sourceId
        ... (8 more members)
    }
```

```{mermaid}
:caption: Spritemanager

classDiagram
    class SpriteManager {
        +terminate()
        +loadSpr()
        +unload()
        +saveSpr()
        +saveSpr64()
        +encryptSprites()
        +dumpSprites()
        +getSignature()
        +getSpritesCount()
        +getSpriteImage()
        +isLoaded()
        +spriteSize()
        +getOffsetFactor()
        +isHdMod()
    }
```

```{mermaid}
:caption: Statictext

classDiagram
    class StaticTextMessage {
    }
    class StaticText {
        +drawText()
        +getName()
        +getText()
        +getMessageMode()
        +getFirstMessage()
        +isYell()
        +setText()
        +setFont()
        +addMessage()
        +addColoredMessage()
        +asStaticText()
        +isStaticText()
        +setColor()
        +getColor()
        +hasText()
    }
```

```{mermaid}
:caption: Stats

classDiagram
    class Stat {
    }
    class StatsData {
    }
    class UIWidget {
        +add()
        +get()
        +clear()
        +clearAll()
        +getSlow()
        +clearSlow()
        +types()
        +getSleepTime()
        +m_sleepTime
        +resetSleepTime()
        +m_sleepTime
        +addWidget()
        +removeWidget()
        +getWidgetsInfo()
        +addTexture()
        +removeTexture()
        +addThing()
        +removeThing()
        +addCreature()
        +removeCreature()
    }
    class Stats {
    }
    class AutoStat {
    }
```

```{mermaid}
:caption: Streamsoundsource

classDiagram
    class StreamSoundSource {
        +play()
        +stop()
        +isPlaying()
        +setSoundFile()
        +downMix()
        +update()
    }
```

```{mermaid}
:caption: Textrender

classDiagram
    class TextRenderCache {
    }
    class TextRender {
        +init()
        +terminate()
        +poll()
        +addText()
        +drawText()
        +drawText()
        +drawColoredText()
    }
```

```{mermaid}
:caption: Texture

classDiagram
    class Texture {
        +replace()
        +resize()
        +update()
        +setUpsideDown()
        +setSmooth()
        +setRepeat()
        +buildHardwareMipmaps()
        +setTime()
        +setCanCache()
        +getId()
        +getUniqueId()
        +getTime()
        +getWidth()
        +getHeight()
        +isEmpty()
        +hasRepeat()
        +hasMipmaps()
        +canCache()
        +isAnimatedTexture()
        #uploadPixels()
        ... (18 more members)
    }
```

```{mermaid}
:caption: Texturemanager

classDiagram
    class TextureManager {
        +init()
        +terminate()
        +clearCache()
        +reload()
        +preload()
        +getTexture()
        +loadTexture()
    }
```

```{mermaid}
:caption: Thing

classDiagram
    class Thing {
        +draw()
        +setId()
        +setPosition()
        +getId()
        +getPosition()
        +getStackPriority()
        +getParentContainer()
        +getStackPos()
        +setMarked()
        +updatedMarkedColor()
        +isItem()
        +isEffect()
        +isMissile()
        +isCreature()
        +isNpc()
        +isMonster()
        +isPlayer()
        +isLocalPlayer()
        +isAnimatedText()
        +isStaticText()
        ... (73 more members)
    }
```

```{mermaid}
:caption: Thingstype

classDiagram
    class ThingsType {
        +load()
        +unload()
        +parseThingType()
        +getSignature()
        +isLoaded()
        +getFirstItemId()
        +getMaxItemid()
        +isValidItemId()
    }
```

```{mermaid}
:caption: Thingtype

classDiagram
    class MarketData {
    }
    class StoreCategory {
    }
    class StoreOffer {
    }
    class Imbuement {
    }
    class Light {
    }
    class DrawOutfitParams {
    }
    class ThingType {
        +unserialize()
        +unserializeOtml()
        +unload()
        +serialize()
        +exportImage()
        +replaceSprites()
        +drawOutfit()
        +getDrawSize()
        +drawWithShader()
        +drawWithShader()
        +getId()
        +getCategory()
        +isNull()
        +hasAttr()
        +isLoaded()
        +getLastUsage()
        +getSize()
        +getWidth()
        +getHeight()
        +getExactSize()
        ... (63 more members)
    }
    class DrawQueueItemThingWithShader {
    }
```

```{mermaid}
:caption: Thingtypemanager

classDiagram
    class ThingTypeManager {
        +init()
        +terminate()
        +check()
        +loadDat()
        +loadOtml()
        +loadOtb()
        +loadXml()
        +parseItemType()
        +saveDat()
        +dumpTextures()
        +replaceTextures()
        +addItemType()
        +findItemTypesByName()
        +findItemTypesByString()
        +getMarketCategories()
        +m_marketCategories
        +findThingTypeByAttr()
        +findItemTypeByCategory()
        +getDatSignature()
        +getOtbMajorVersion()
        ... (7 more members)
    }
```

```{mermaid}
:caption: Tile

classDiagram
    class Tile {
        +calculateCorpseCorrection()
        +drawGround()
        +drawBottom()
        +drawCreatures()
        +drawTop()
        +drawTexts()
        +drawWidget()
        +clean()
        +addWalkingCreature()
        +removeWalkingCreature()
        +addThing()
        +removeThing()
        +getThing()
        +getEffect()
        +hasThing()
        +getThingStackPos()
        +getTopThing()
        +getTopLookThing()
        +getTopLookThingEx()
        +getTopUseThing()
        ... (59 more members)
    }
```

```{mermaid}
:caption: Time

classDiagram
    class timer {
    }
```

```{mermaid}
:caption: Timer

classDiagram
    class Timer {
        +restart()
        +stop()
        +adjust()
        +startTicks()
        +ticksElapsed()
        +timeElapsed()
        +running()
    }
```

```{mermaid}
:caption: Tinystr

classDiagram
    class TiXmlString {
    }
    class Rep {
    }
    class TiXmlOutStream {
    }
```

```{mermaid}
:caption: Towns

classDiagram
    class Town {
        +setId()
        +setName()
        +setPos()
        +getId()
        +getName()
        +getPos()
    }
    class TownManager {
        +addTown()
        +removeTown()
        +sort()
        +getTowns()
        +clear()
        #findTown()
    }
```

```{mermaid}
:caption: Uianchorlayout

classDiagram
    class UIAnchor {
        +getAnchoredEdge()
        +getHookedEdge()
        +getHookedWidget()
        +getHookedPoint()
        #m_anchoredEdge
        #m_hookedEdge
        #m_hookedWidgetId
    }
    class UIAnchorGroup {
        +addAnchor()
        +isUpdated()
        +setUpdated()
    }
    class UIAnchorLayout {
        +removeAnchors()
        +hasAnchors()
        +centerIn()
        +fill()
        +addWidget()
        +removeWidget()
        +isUIAnchorLayout()
        #internalUpdate()
        #updateWidget()
        #m_anchorsGroups
    }
```

```{mermaid}
:caption: Uiboxlayout

classDiagram
    class UIBoxLayout {
        +applyStyle()
        +addWidget()
        +removeWidget()
        +setSpacing()
        +setFitChildren()
        +isUIBoxLayout()
        #m_fitChildren
        #m_spacing
    }
```

```{mermaid}
:caption: Uicreature

classDiagram
    class UICreature {
        +drawSelf()
        +setCreature()
        +setFixedCreatureSize()
        +setOutfit()
        +getCreature()
        +getOutfit()
        +isFixedCreatureSize()
        +setAutoRotating()
        +setDirection()
        +getDirection()
        +setScale()
        +getScale()
        +setAnimate()
        +isAnimating()
        +setCenter()
        +setOldScaling()
        #onStyleApply()
        #onGeometryChange()
        #m_creature
        #m_autoRotating
        ... (4 more members)
    }
```

```{mermaid}
:caption: Uigraph

classDiagram
    class UIGraph {
    }
```

```{mermaid}
:caption: Uigridlayout

classDiagram
    class UIGridLayout {
        +applyStyle()
        +removeWidget()
        +addWidget()
        +setCellSize()
        +setCellWidth()
        +setCellHeight()
        +setCellSpacing()
        +setNumColumns()
        +setNumLines()
        +setAutoSpacing()
        +setFitChildren()
        +setFlow()
        +getCellSize()
        +getCellSpacing()
        +getNumColumns()
        +getNumLines()
        +isUIGridLayout()
        #internalUpdate()
    }
```

```{mermaid}
:caption: Uihorizontallayout

classDiagram
    class UIHorizontalLayout {
        +applyStyle()
        +setAlignRight()
        +isUIHorizontalLayout()
        #internalUpdate()
        #m_alignChidren
        #m_alignRight
    }
```

```{mermaid}
:caption: Uiitem

classDiagram
    class UIItem {
        +drawSelf()
        +setItemId()
        +setItemCount()
        +setItemSubType()
        +setItemVisible()
        +setItem()
        +setVirtual()
        +clearItem()
        +setShowCount()
        +setItemShader()
        +getItemId()
        +getItemCount()
        +getItemSubType()
        +getItemCountOrSubType()
        +getItem()
        +isVirtual()
        +isItemVisible()
        #onStyleApply()
        #cacheCountText()
        #m_item
        ... (6 more members)
    }
```

```{mermaid}
:caption: Uilayout

classDiagram
    class UILayout {
        +update()
        +updateLater()
        +applyStyle()
        +addWidget()
        +removeWidget()
        +disableUpdates()
        +enableUpdates()
        +setParent()
        +getParentWidget()
        +isUpdateDisabled()
        +isUpdating()
        +isUIAnchorLayout()
        +isUIBoxLayout()
        +isUIHorizontalLayout()
        +isUIVerticalLayout()
        +isUIGridLayout()
        #internalUpdate()
        #m_updateDisabled
        #m_updating
        #m_updateScheduled
        ... (1 more members)
    }
```

```{mermaid}
:caption: Uimanager

classDiagram
    class UIManager {
        +init()
        +terminate()
        +render()
        +resize()
        +inputEvent()
        +updatePressedWidget()
        +updateDraggingWidget()
        +updateHoveredWidget()
        +clearStyles()
        +importStyle()
        +importStyleFromString()
        +importStyleFromOTML()
        +getStyle()
        +getStyleClass()
        +loadUIFromString()
        +loadUI()
        +displayUI()
        +createWidget()
        +createWidgetFromOTML()
        +setMouseReceiver()
        ... (16 more members)
    }
```

```{mermaid}
:caption: Uimap

classDiagram
    class UIMap {
        +onMouseMove()
        +drawSelf()
        +movePixels()
        +setZoom()
        +zoomIn()
        +zoomOut()
        +followCreature()
        +setCameraPosition()
        +setMaxZoomIn()
        +setMaxZoomOut()
        +setMultifloor()
        +lockVisibleFloor()
        +unlockVisibleFloor()
        +setVisibleDimension()
        +setDrawFlags()
        +setDrawTexts()
        +setDrawNames()
        +setDrawHealthBars()
        +setDrawHealthBarsOnTop()
        +setDrawLights()
        ... (34 more members)
    }
```

```{mermaid}
:caption: Uimapanchorlayout

classDiagram
    class UIPositionAnchor {
        +getHookedWidget()
        +getHookedPoint()
    }
    class UIMapAnchorLayout {
        +centerInPosition()
        +fillPosition()
    }
```

```{mermaid}
:caption: Uiminimap

classDiagram
    class UIMinimap {
        +drawSelf()
        +zoomIn()
        +zoomOut()
        +setZoom()
        +setMinZoom()
        +setMaxZoom()
        +setCameraPosition()
        +floorUp()
        +floorDown()
        +getTilePoint()
        +getTileRect()
        +getTilePosition()
        +getCameraPosition()
        +getMinZoom()
        +getMaxZoom()
        +getZoom()
        +getScale()
        +anchorPosition()
        +fillPosition()
        +centerInPosition()
        ... (3 more members)
    }
```

```{mermaid}
:caption: Uiprogressrect

classDiagram
    class UIProgressRect {
        +drawSelf()
        +setPercent()
        +getPercent()
        #onStyleApply()
        #m_percent
    }
```

```{mermaid}
:caption: Uisprite

classDiagram
    class UISprite {
        +drawSelf()
        +setSpriteId()
        +getSpriteId()
        +clearSprite()
        +setSpriteColor()
        +isSpriteVisible()
        +setSpriteVisible()
        +hasSprite()
        #onStyleApply()
        #m_sprite
        #m_spriteId
        #m_spriteColor
        #m_spriteVisible
    }
```

```{mermaid}
:caption: Uitextedit

classDiagram
    class UITextEdit {
        +drawSelf()
        +setCursorPos()
        +setSelection()
        +setCursorVisible()
        +setTextHidden()
        +setValidCharacters()
        +setShiftNavigation()
        +setMultiline()
        +setMaxLength()
        +setTextVirtualOffset()
        +setEditable()
        +setSelectable()
        +setSelectionColor()
        +setSelectionBackgroundColor()
        +setAutoScroll()
        +setAutoSubmit()
        +setPlaceholder()
        +setPlaceholderColor()
        +setPlaceholderAlign()
        +setPlaceholderFont()
        ... (44 more members)
    }
```

```{mermaid}
:caption: Uiverticallayout

classDiagram
    class UIVerticalLayout {
        +applyStyle()
        +setAlignBottom()
        +isAlignBottom()
        +isUIVerticalLayout()
        #internalUpdate()
        #m_alignBottom
    }
```

```{mermaid}
:caption: Uiwidget

classDiagram
    class EdgeGroup {
    }
    class UIWidget {
        +draw()
        #drawSelf()
        #drawChildren()
        #m_id
        #m_source
        #m_rect
        #m_virtualOffset
        #m_autoDraw
        #m_enabled
        #m_visible
        #m_focusable
        #m_fixedSize
        #m_phantom
        #m_draggable
        #m_destroyed
        #m_clipping
        #m_layout
        #m_parent
        #m_parentId
        #m_children
        ... (374 more members)
    }
```

```{mermaid}
:caption: Uri

classDiagram
    class ParsedURI {
    }
```

```{mermaid}
:caption: Vertexarray

classDiagram
    class VertexArray {
        +m_hardwareBuffer
        +addVertex()
        +addTriangle()
        +addRect()
        +top
        +right
        +bottom
        +left
        +addRect()
        +top
        +right
        +bottom
        +left
        +addQuad()
        +top
        +right
        +bottom
        +left
        +addUpsideDownQuad()
        +top
        ... (8 more members)
    }
```

```{mermaid}
:caption: Walkmatrix

classDiagram
    class WalkMatrix {
    }
```

```{mermaid}
:caption: Websocket

classDiagram
    class WebsocketSession {
        +start()
        +send()
        +close()
    }
```

```{mermaid}
:caption: Win32Window

classDiagram
    class WindowProcProxy {
        +init()
        +terminate()
        +move()
        +resize()
        +show()
        +hide()
        +minimize()
        +maximize()
        +poll()
        +swapBuffers()
        +showMouse()
        +hideMouse()
        +displayFatalError()
        +setMouseCursor()
        +restoreMouseCursor()
        +setTitle()
        +setMinimumSize()
        +setFullscreen()
        +setVerticalSync()
        +setIcon()
        ... (6 more members)
    }
    class WIN32Window {
        +init()
        +terminate()
        +move()
        +resize()
        +show()
        +hide()
        +minimize()
        +maximize()
        +poll()
        +swapBuffers()
        +showMouse()
        +hideMouse()
        +displayFatalError()
        +setMouseCursor()
        +restoreMouseCursor()
        +setTitle()
        +setMinimumSize()
        +setFullscreen()
        +setVerticalSync()
        +setIcon()
        ... (6 more members)
    }
```

```{mermaid}
:caption: X11Window

classDiagram
    class X11Window {
        +init()
        +terminate()
        +move()
        +resize()
        +show()
        +hide()
        +minimize()
        +maximize()
        +poll()
        +swapBuffers()
        +showMouse()
        +hideMouse()
        +setMouseCursor()
        +restoreMouseCursor()
        +setTitle()
        +setMinimumSize()
        +setFullscreen()
        +setVerticalSync()
        +setIcon()
        +setClipboardText()
        ... (5 more members)
    }
```


## Diagrams

```{mermaid}
:caption: Adaptiverenderer

classDiagram
    class AdaptiveRenderer {
    }
```

```{mermaid}
:caption: Android Native App Glue

classDiagram
    class android_app {
    }
    class android_poll_source {
    }
    class android_app {
    }
    class android_app {
    }
    class android_poll_source {
    }
    class android_poll_source {
    }
```

```{mermaid}
:caption: Androidwindow

classDiagram
    class AndroidWindow {
    }
```

```{mermaid}
:caption: Animatedtext

classDiagram
    class AnimatedText {
        +drawText()
        +setColor()
        +setText()
        +setOffset()
        +setFont()
        +getColor()
        +getOffset()
        +getTimer()
        +merge()
        +asAnimatedText()
        +isAnimatedText()
        +getText()
        #onAppear()
    }
```

```{mermaid}
:caption: Animatedtexture

classDiagram
    class AnimatedTexture {
        +replace()
        +update()
        +isAnimatedTexture()
        #buildHardwareMipmaps()
        #setSmooth()
        #setRepeat()
    }
```

```{mermaid}
:caption: Animator

classDiagram
    class Animator {
        +unserialize()
        +serialize()
        +setPhase()
        +getPhase()
        +getPhaseAt()
        +getStartPhase()
        +getAnimationPhases()
        +isAsync()
        +isComplete()
        +getTotalDuration()
        +resetAnimation()
    }
```

```{mermaid}
:caption: Any

classDiagram
    class any {
    }
    class placeholder {
    }
    class holder {
    }
```

```{mermaid}
:caption: Apngloader

classDiagram
    class apng_data {
    }
```

```{mermaid}
:caption: Application

classDiagram
    class Application {
        +init()
        +deinit()
        +terminate()
        +run()
        +poll()
        +exit()
        +quick_exit()
        +close()
        +restart()
        +restartArgs()
        +setName()
        +setCompactName()
        +setVersion()
        +isRunning()
        +isStopping()
        +isTerminated()
        +getCharset()
        +getBuildCompiler()
        +getBuildDate()
        +getBuildRevision()
        ... (19 more members)
    }
```

```{mermaid}
:caption: Asyncdispatcher

classDiagram
    class AsyncDispatcher {
    }
```

```{mermaid}
:caption: Atlas

classDiagram
    class Atlas {
    }
```

```{mermaid}
:caption: Binarytree

classDiagram
    class BinaryTree {
        +seek()
        +skip()
        +tell()
        +size()
        +getU8()
        +getU16()
        +getU32()
        +getU64()
        +getString()
        +getPoint()
        +getChildren()
        +canRead()
    }
    class OutputBinaryTree {
        +addU8()
        +addU16()
        +addU32()
        +addString()
        +addPos()
        +addPoint()
        +startNode()
        +endNode()
        #write()
    }
```

```{mermaid}
:caption: Bitmapfont

classDiagram
    class BitmapFont {
        +load()
        +drawText()
        +drawText()
        +drawColoredText()
        +calculateDrawTextCoords()
        +align
        +calculateTextRectSize()
        +wrapText()
        +getId()
        +getName()
        +getGlyphHeight()
        +getYOffset()
        +getGlyphSpacing()
    }
```

```{mermaid}
:caption: Boolean

classDiagram
    class boolean {
    }
```

```{mermaid}
:caption: Cachedtext

classDiagram
    class CachedText {
        +draw()
        +wrapText()
        +setFont()
        +setText()
        +setColoredText()
        +setAlign()
        +getTextSize()
        +getText()
        +getFont()
        +getAlign()
        +hasText()
    }
```

```{mermaid}
:caption: Cast

classDiagram
    class cast_exception {
    }
```

```{mermaid}
:caption: Client

classDiagram
    class Client {
        +init()
        +terminate()
        +registerLuaFunctions()
    }
```

```{mermaid}
:caption: Clock

classDiagram
    class Clock {
        +update()
        +micros()
        +millis()
        +seconds()
        +realMicros()
        +realMillis()
    }
```

```{mermaid}
:caption: Color

classDiagram
    class Color {
        +a()
        +b()
        +g()
        +r()
        +aF()
        +bF()
        +gF()
        +rF()
        +setRed()
        +setGreen()
        +setBlue()
        +setAlpha()
        +setRed()
        +setGreen()
        +setBlue()
        +setAlpha()
        +setRGBA()
        +setRGBA()
        +opacity()
        +Color()
        ... (14 more members)
    }
```

```{mermaid}
:caption: Colorarray

classDiagram
    class ColorArray {
        +addColor()
        +addColor()
        +clear()
        +colorCount()
        +count()
        +size()
    }
```

```{mermaid}
:caption: Combinedsoundsource

classDiagram
    class CombinedSoundSource {
        +addSource()
        +getSources()
        +play()
        +stop()
        +isBuffering()
        +isPlaying()
        +setLooping()
        +setRelative()
        +setReferenceDistance()
        +setGain()
        +setPitch()
        +setPosition()
        +setVelocity()
        +setFading()
        #update()
    }
```

```{mermaid}
:caption: Config

classDiagram
    class Config {
        +load()
        +unload()
        +save()
        +clear()
        +setValue()
        +setList()
        +getValue()
        +getList()
        +setNode()
        +mergeNode()
        +getNode()
        +getNodeSize()
        +exists()
        +remove()
        +getFileName()
        +isLoaded()
        +asConfig()
    }
```

```{mermaid}
:caption: Configmanager

classDiagram
    class ConfigManager {
        +init()
        +terminate()
        +getSettings()
        +get()
        +create()
        +loadSettings()
        +load()
        +unload()
        +remove()
        #m_settings
    }
```

```{mermaid}
:caption: Connection

classDiagram
    class Connection {
        +poll()
        +terminate()
        +connect()
        +close()
        +write()
        +read()
        +read_until()
        +read_some()
        +setErrorCallback()
        +getIp()
        +getError()
        +isConnecting()
        +isConnected()
        +getElapsedTicksSinceLastRead()
        +asConnection()
        #internal_connect()
        #internal_write()
        #onResolve()
        #onConnect()
        #onCanWrite()
        ... (18 more members)
    }
```

```{mermaid}
:caption: Consoleapplication

classDiagram
    class ConsoleApplication {
        +run()
    }
```

```{mermaid}
:caption: Container

classDiagram
    class Container {
        +getItem()
        +getItems()
        +getItemsCount()
        +getSlotPosition()
        +getId()
        +getCapacity()
        +getContainerItem()
        +getName()
        +hasParent()
        +isClosed()
        +isUnlocked()
        +hasPages()
        +getSize()
        +getFirstIndex()
        +findItemById()
        #onOpen()
        #onClose()
        #onAddItem()
        #onAddItems()
        #onUpdateItem()
        ... (1 more members)
    }
```

```{mermaid}
:caption: Coordsbuffer

classDiagram
    class CoordsBuffer {
        +clear()
        +addTriangle()
        +addRect()
        +addRect()
        +addRect()
        +addQuad()
        +addUpsideDownQuad()
        +addBoudingRect()
        +addRepeatedRects()
        +getVertexCount()
        +getTextureCoordCount()
        +unlock()
        +cache()
        +getTextureRect()
    }
```

```{mermaid}
:caption: Creature

classDiagram
    class Creature {
        +draw()
        +drawOutfit()
        +drawInformation()
        +isInsideOffset()
        +setId()
        +setName()
        +setManaPercent()
        +setHealthPercent()
        +setDirection()
        +setOutfit()
        +setOutfitColor()
        +setLight()
        +setSpeed()
        +setBaseSpeed()
        +setSkull()
        +setShield()
        +setEmblem()
        +setType()
        +setIcon()
        +setSkullTexture()
        ... (175 more members)
    }
    class Npc {
        +isNpc()
    }
    class Monster {
        +isMonster()
    }
```

```{mermaid}
:caption: Creatures

classDiagram
    class Spawn {
        +setRadius()
        +getRadius()
        +setCenterPos()
        +getCenterPos()
        +getCreatures()
        +addCreature()
        +removeCreature()
        +clear()
        #load()
        #save()
    }
    class CreatureType {
        +setSpawnTime()
        +getSpawnTime()
        +setName()
        +getName()
        +setOutfit()
        +getOutfit()
        +setDirection()
        +getDirection()
        +setRace()
        +getRace()
        +cast()
    }
    class CreatureManager {
        +clear()
        +clearSpawns()
        +terminate()
        +loadMonsters()
        +loadSingleCreature()
        +loadNpcs()
        +loadCreatureBuffer()
        +loadSpawns()
        +saveSpawns()
        +getSpawns()
        +getSpawn()
        +getSpawnForPlacePos()
        +addSpawn()
        +deleteSpawn()
        +isLoaded()
        +isSpawnLoaded()
        #internalLoadCreatureBuffer()
    }
```

```{mermaid}
:caption: Crypt

classDiagram
    class Crypt {
        +base64Encode()
        +base64Decode()
        +xorCrypt()
        +encrypt()
        +decrypt()
        +genUUID()
        +setMachineUUID()
        +getMachineUUID()
        +md5Encode()
        +sha1Encode()
        +sha256Encode()
        +sha512Encode()
        +crc32()
        +rsaGenerateKey()
        +rsaSetPublicKey()
        +rsaSetPrivateKey()
        +rsaCheckKey()
        +rsaEncrypt()
        +rsaDecrypt()
        +rsaGetSize()
        ... (2 more members)
    }
```

```{mermaid}
:caption: Databuffer

classDiagram
    class DataBuffer {
        +reset()
        +clear()
        +empty()
        +size()
        +reserve()
        +resize()
        +grow()
        +newcapacity
        +add()
    }
```

```{mermaid}
:caption: Declarations

classDiagram
    class UIManager {
    }
    class UIWidget {
    }
    class UITextEdit {
    }
    class UILayout {
    }
    class UIBoxLayout {
    }
    class UIHorizontalLayout {
    }
    class UIVerticalLayout {
    }
    class UIGridLayout {
    }
    class UIAnchor {
    }
    class UIAnchorGroup {
    }
    class UIAnchorLayout {
    }
```

```{mermaid}
:caption: Deptharray

classDiagram
    class DepthArray {
        +addDepth()
        +clear()
        +depthCount()
        +count()
        +size()
    }
```

```{mermaid}
:caption: Drawcache

classDiagram
    class DrawCache {
    }
```

```{mermaid}
:caption: Drawqueue

classDiagram
    class DrawQueue {
    }
    class DrawQueueItem {
    }
    class DrawQueueItem {
    }
    class DrawQueueItemTexturedRect {
    }
    class DrawQueueItemTextureCoords {
    }
    class DrawQueueItemColoredTextureCoords {
    }
    class DrawQueueItemImageWithShader {
    }
    class DrawQueueItemFilledRect {
    }
    class DrawQueueItemClearRect {
    }
    class DrawQueueItemFillCoords {
    }
    class DrawQueueItemText {
    }
    class DrawQueueItemTextColored {
    }
    class DrawQueueItemLine {
    }
    class DrawQueueCondition {
    }
    class DrawQueueConditionClip {
    }
    class DrawQueueConditionRotation {
    }
    class DrawQueueConditionMark {
    }
    class DrawQueue {
    }
```

```{mermaid}
:caption: Dumper

classDiagram
    class dumper_dummy {
    }
```

```{mermaid}
:caption: Dynamic Storage

classDiagram
    class dynamic_storage {
    }
```

```{mermaid}
:caption: Effect

classDiagram
    class Effect {
        +draw()
        +draw()
        +setId()
        +getId()
        +asEffect()
        +isEffect()
        #onAppear()
    }
```

```{mermaid}
:caption: Event

classDiagram
    class Event {
        +execute()
        +cancel()
        +isCanceled()
        +isExecuted()
        +isBotSafe()
        #m_function
        #m_callback
        #m_canceled
        #m_executed
        #m_botSafe
    }
```

```{mermaid}
:caption: Eventdispatcher

classDiagram
    class EventDispatcher {
        +shutdown()
        +poll()
        +addEventEx()
        +scheduleEventEx()
        +cycleEventEx()
        +isBotSafe()
    }
```

```{mermaid}
:caption: Exception

classDiagram
    class exception {
        #m_what
    }
```

```{mermaid}
:caption: Extras

classDiagram
    class Extras {
    }
```

```{mermaid}
:caption: Filestream

classDiagram
    class PHYSFS_File {
        +close()
        +flush()
        +write()
        +read()
        +seek()
        +skip()
        +size()
        +tell()
        +eof()
        +name()
        +getU8()
        +getU16()
        +getU32()
        +getU64()
        +get8()
        +get16()
        +get32()
        +get64()
        +getString()
        +getBinaryTree()
        ... (14 more members)
    }
    class FileStream {
        +close()
        +flush()
        +write()
        +read()
        +seek()
        +skip()
        +size()
        +tell()
        +eof()
        +name()
        +getU8()
        +getU16()
        +getU32()
        +getU64()
        +get8()
        +get16()
        +get32()
        +get64()
        +getString()
        +getBinaryTree()
        ... (14 more members)
    }
```

```{mermaid}
:caption: Fontmanager

classDiagram
    class FontManager {
        +terminate()
        +clearFonts()
        +importFont()
        +fontExists()
        +getFont()
        +getDefaultFont()
        +setDefaultFont()
    }
```

```{mermaid}
:caption: Framebuffer

classDiagram
    class FrameBuffer {
        +resize()
        +bind()
        +release()
        +draw()
        +draw()
        +draw()
        +setSmooth()
        +getTexture()
        +getSize()
        +isSmooth()
        +getDepthRenderBuffer()
        +hasDepth()
        +readPixels()
        +doScreenshot()
    }
```

```{mermaid}
:caption: Framebuffermanager

classDiagram
    class FrameBufferManager {
        +init()
        +terminate()
        +clear()
        +createFrameBuffer()
        #m_temporaryFramebuffer
        #m_drawQueueTemporaryFramebuffer
        #m_framebuffers
    }
```

```{mermaid}
:caption: Framecounter

classDiagram
    class FrameCounter {
    }
```

```{mermaid}
:caption: Game

classDiagram
    class UnjustifiedPoints {
    }
    class Game {
        +init()
        +terminate()
        #processConnectionError()
        #processDisconnect()
        #processPing()
        #processPingBack()
        #processNewPing()
        #processUpdateNeeded()
        #processLoginError()
        #processLoginAdvice()
        #processLoginWait()
        #processLoginToken()
        #processLogin()
        #processPendingGame()
        #processEnterGame()
        #processGameStart()
        #processGameEnd()
        #processDeath()
        #processGMActions()
        #processInventoryChange()
        ... (205 more members)
    }
```

```{mermaid}
:caption: Graph

classDiagram
    class Graph {
        +draw()
        +clear()
        +addValue()
    }
```

```{mermaid}
:caption: Graphicalapplication

classDiagram
    class GraphicalApplication {
        +init()
        +deinit()
        +terminate()
        +run()
        +poll()
        +pollGraphics()
        +close()
        +willRepaint()
        +repaint()
        +setMaxFps()
        +getMaxFps()
        +getFps()
        +getGraphicsFps()
        +getProcessingFps()
        +isOnInputEvent()
        +getIteration()
        +m_iteration
        +doScreenshot()
        +scaleUp()
        +scaleDown()
        ... (5 more members)
    }
```

```{mermaid}
:caption: Graphics

classDiagram
    class Painter {
        +init()
        +terminate()
        +resize()
        +checkDepthSupport()
        +getMaxTextureSize()
        +getVendor()
        +getRenderer()
        +getVersion()
        +getExtensions()
        +ok()
        +checkForError()
    }
    class Graphics {
        +init()
        +terminate()
        +resize()
        +checkDepthSupport()
        +getMaxTextureSize()
        +getVendor()
        +getRenderer()
        +getVersion()
        +getExtensions()
        +ok()
        +checkForError()
    }
```

```{mermaid}
:caption: Hardwarebuffer

classDiagram
    class HardwareBuffer {
        +bind()
        +unbind()
        +write()
    }
```

```{mermaid}
:caption: Healthbars

classDiagram
    class HealthBar {
        +setPath()
        +getPath()
        +setTexture()
        +getTexture()
        +setOffset()
        +getOffset()
        +setBarOffset()
        +getBarOffset()
        +setHeight()
        +getHeight()
    }
    class HealthBars {
        +init()
        +terminate()
        +addHealthBackground()
        +addManaBackground()
        +getHealthBar()
        +getManaBar()
        +getHealthBarPath()
        +getManaBarPath()
        +getHealthBarOffset()
        +getManaBarOffset()
        +getHealthBarOffsetBar()
        +getManaBarOffsetBar()
        +getHealthBarHeight()
        +getManaBarHeight()
    }
```

```{mermaid}
:caption: Houses

classDiagram
    class House {
        +setTile()
        +getTile()
        +setName()
        +getName()
        +setId()
        +getId()
        +setTownId()
        +getTownId()
        +setSize()
        +getSize()
        +setRent()
        +getRent()
        +setEntry()
        +getEntry()
        +addDoor()
        +removeDoor()
        +removeDoorById()
        #load()
        #save()
    }
    class HouseManager {
    }
```

```{mermaid}
:caption: Http

classDiagram
    class WebsocketSession {
        +init()
        +terminate()
        +get()
        +post()
        +download()
        +ws()
        +wsSend()
        +wsClose()
        +cancel()
        +m_downloads
        +clearDownloads()
        +getFile()
        +it
        +nullptr
        +setUserAgent()
    }
    class Http {
    }
```

```{mermaid}
:caption: Image

classDiagram
    class Image {
        +load()
        +loadPNG()
        +loadPNG()
        +savePNG()
        +blit()
        +paste()
        +upscale()
        +resize()
        +nextMipmap()
        +setPixel()
        +setPixel()
        +setPixel()
        +getPixelCount()
        +getWidth()
        +getHeight()
        +getBpp()
        +fromQRCode()
    }
```

```{mermaid}
:caption: Inputevent

classDiagram
    class InputEvent {
    }
```

```{mermaid}
:caption: Inputmessage

classDiagram
    class InputMessage {
        +setBuffer()
        +getBuffer()
        +getBodyBuffer()
        +skipBytes()
        +setReadPos()
        +getU8()
        +getU16()
        +getU32()
        +getU64()
        +getString()
        +getDouble()
        +peekU8()
        +peekU16()
        +peekU32()
        +peekU64()
        +decryptRsa()
        +getHeaderPos()
        +getHeaderSize()
        +getReadSize()
        +getReadPos()
        ... (10 more members)
    }
```

```{mermaid}
:caption: Item

classDiagram
    class Item {
        +create()
        +createFromOtb()
        +draw()
        +draw()
        +setId()
        +setOtbId()
        +setCountOrSubType()
        +setCount()
        +setSubType()
        +setColor()
        +setTooltip()
        +setQuickLootFlags()
        +setShader()
        +getCountOrSubType()
        +getSubType()
        +getCount()
        +getId()
        +getClientId()
        +getServerId()
        +getName()
        ... (42 more members)
    }
```

```{mermaid}
:caption: Itemtype

classDiagram
    class ItemType {
        +unserialize()
        +setServerId()
        +getServerId()
        +setClientId()
        +getClientId()
        +setCategory()
        +getCategory()
        +setName()
        +getName()
        +setDesc()
        +getDesc()
        +isNull()
        +isWritable()
    }
```

```{mermaid}
:caption: Lbitlib

classDiagram
    class lua_State {
    }
```

```{mermaid}
:caption: Lightview

classDiagram
    class TileLight {
    }
    class LightView {
        +addLight()
        +addLight()
        +addLight()
        +setFieldBrightness()
        +size()
        +draw()
    }
```

```{mermaid}
:caption: Localplayer

classDiagram
    class LocalPlayer {
        +draw()
        +unlockWalk()
        +lockWalk()
        +stopAutoWalk()
        +autoWalk()
        +canWalk()
        +isWalkLocked()
        +turn()
        +setStates()
        +setSkill()
        +setBaseSkill()
        +setHealth()
        +setFreeCapacity()
        +setTotalCapacity()
        +setExperience()
        +setLevel()
        +setMana()
        +setMagicLevel()
        +setBaseMagicLevel()
        +setSoul()
        ... (64 more members)
    }
```

```{mermaid}
:caption: Logger

classDiagram
    class LogMessage {
    }
    class Logger {
        +log()
        +logFunc()
        +debug()
        +info()
        +warning()
        +error()
        +fatal()
        +fireOldMessages()
        +setLogFile()
        +setOnLog()
        +getLastLog()
        +m_lastLog
        +setTestingMode()
    }
```

```{mermaid}
:caption: Luabinder

classDiagram
    class pack_values_into_tuple {
    }
    class pack_values_into_tuple {
    }
    class expand_fun_arguments {
    }
    class expand_fun_arguments {
    }
    class bind_lambda_fun {
    }
    class bind_lambda_fun {
    }
```

```{mermaid}
:caption: Luaexception

classDiagram
    class LuaException {
        +generateLuaErrorMessage()
        #m_what
    }
    class LuaBadNumberOfArgumentsException {
    }
    class LuaBadValueCastException {
    }
```

```{mermaid}
:caption: Luainterface

classDiagram
    class lua_State {
        +init()
        +terminate()
        +registerFunctions()
        +registerSingletonClass()
        +registerClass()
        +registerClass()
        +registerClassStaticFunction()
        +registerClassMemberFunction()
        +bindSingletonFunction()
        +bindSingletonFunction()
        +bindSingletonFunction()
        +bindClassStaticFunction()
        +bindClassStaticFunction()
        +bindClassMemberFunction()
        +bindClassMemberFunction()
        +bindClassMemberField()
        +bindClassMemberField()
        +bindClassMemberGetField()
        +bindClassMemberGetField()
        +bindClassMemberSetField()
        ... (105 more members)
    }
    class LuaInterface {
        +init()
        +terminate()
        +registerFunctions()
        +registerSingletonClass()
        +registerClass()
        +registerClass()
        +registerClassStaticFunction()
        +registerClassMemberFunction()
        +bindSingletonFunction()
        +bindSingletonFunction()
        +bindSingletonFunction()
        +bindClassStaticFunction()
        +bindClassStaticFunction()
        +bindClassMemberFunction()
        +bindClassMemberFunction()
        +bindClassMemberField()
        +bindClassMemberField()
        +bindClassMemberGetField()
        +bindClassMemberGetField()
        +bindClassMemberSetField()
        ... (105 more members)
    }
```

```{mermaid}
:caption: Luaobject

classDiagram
    class LuaObject {
        +connectLuaField()
        +luaCallLuaField()
        +callLuaField()
        +callLuaField()
        +hasLuaField()
        +setLuaField()
        +getLuaField()
        +releaseLuaFieldsTable()
        +luaSetField()
        +luaGetField()
        +luaGetMetatable()
        +luaGetFieldsTable()
        +getUseCount()
        +getClassName()
        +asLuaObject()
        +operator
    }
    class connect_lambda {
    }
    class connect_lambda {
    }
```

```{mermaid}
:caption: Luavaluecasts

classDiagram
    class push_tuple_internal_luavalue {
    }
    class push_tuple_internal_luavalue {
    }
    class push_tuple_luavalue {
    }
    class push_tuple_luavalue {
    }
```

```{mermaid}
:caption: Map

classDiagram
    class TileBlock {
    }
    class AwareRange {
    }
    class PathFindResult {
    }
    class Node {
    }
    class Map {
        +init()
        +terminate()
        +addMapView()
        +removeMapView()
        +notificateTileUpdate()
        +requestVisibleTilesCacheUpdate()
        +loadOtcm()
        +saveOtcm()
        +loadOtbm()
        +saveOtbm()
        +setHouseFile()
        +setSpawnFile()
        +setDescription()
        +clearDescriptions()
        +setWidth()
        +setHeight()
        +getHouseFile()
        +getSpawnFile()
        +getSize()
        +getDescriptions()
        ... (58 more members)
    }
```

```{mermaid}
:caption: Mapview

classDiagram
    class MapView {
        +drawMapBackground()
        +drawMapForeground()
        #onTileUpdate()
        #onMapCenterChange()
        +lockFirstVisibleFloor()
        +unlockFirstVisibleFloor()
        +getLockedFirstVisibleFloor()
        +setMultifloor()
        +isMultifloor()
        +setVisibleDimension()
        +optimizeForSize()
        +getVisibleDimension()
        +getVisibleCenterOffset()
        +getCachedFirstVisibleFloor()
        +getCachedLastVisibleFloor()
        +followCreature()
        +getFollowingCreature()
        +isFollowingCreature()
        +setCameraPosition()
        +getCameraPosition()
        ... (25 more members)
    }
```

```{mermaid}
:caption: Matrix

classDiagram
    class Matrix {
        +setIdentity()
        +isIdentity()
        +fill()
        +transposed()
        +operator()
        +operator
    }
```

```{mermaid}
:caption: Minimap

classDiagram
    class MinimapTile {
    }
    class MinimapBlock {
        +clean()
        +update()
        +updateTile()
        +resetTile()
        +getTileIndex()
        +mustUpdate()
        +justSaw()
        +wasSeen()
    }
    class Minimap {
        +init()
        +terminate()
        +clean()
        +draw()
        +getTilePoint()
        +getTilePosition()
        +getTileRect()
        +updateTile()
        +threadGetTile()
        +loadImage()
        +saveImage()
        +loadOtmm()
        +saveOtmm()
    }
```

```{mermaid}
:caption: Missile

classDiagram
    class Missile {
        +draw()
        +setId()
        +setPath()
        +getId()
        +asMissile()
        +isMissile()
        +getSource()
        +getDestination()
    }
```

```{mermaid}
:caption: Module

classDiagram
    class Module {
        +load()
        +unload()
        +reload()
        +canUnload()
        +canReload()
        +isLoaded()
        +isReloadable()
        +isDependent()
        +isSandboxed()
        +hasDependency()
        +getSandbox()
        +getDescription()
        +getName()
        +getAuthor()
        +getWebsite()
        +getVersion()
        +isAutoLoad()
        +getAutoLoadPriority()
        +asModule()
        #discover()
    }
```

```{mermaid}
:caption: Modulemanager

classDiagram
    class ModuleManager {
        +clear()
        +discoverModules()
        +autoLoadModules()
        +discoverModule()
        +ensureModuleLoaded()
        +unloadModules()
        +reloadModules()
        +getModule()
        +getModules()
        #updateModuleLoadOrder()
    }
```

```{mermaid}
:caption: Mouse

classDiagram
    class Mouse {
        +init()
        +terminate()
        +loadCursors()
        +addCursor()
        +pushCursor()
        +popCursor()
        +isCursorChanged()
        +isPressed()
    }
```

```{mermaid}
:caption: Oggsoundfile

classDiagram
    class OggSoundFile {
        +prepareOgg()
        +read()
        +reset()
    }
```

```{mermaid}
:caption: Otmldocument

classDiagram
    class OTMLDocument {
        +create()
        +parse()
        +parseString()
        +parse()
        +emit()
        +save()
    }
```

```{mermaid}
:caption: Otmlemitter

classDiagram
    class OTMLEmitter {
        +emitNode()
    }
```

```{mermaid}
:caption: Otmlexception

classDiagram
    class OTMLException {
        #m_what
    }
```

```{mermaid}
:caption: Otmlnode

classDiagram
    class OTMLNode {
        +create()
        +create()
        +tag()
        +size()
        +source()
        +rawValue()
        +isUnique()
        +isNull()
        +hasTag()
        +hasValue()
        +hasChildren()
        +hasChildAt()
        +getIndex()
        +setTag()
        +setValue()
        +setNull()
        +setUnique()
        +setSource()
        +setIndex()
        +lockTag()
        ... (27 more members)
    }
```

```{mermaid}
:caption: Otmlparser

classDiagram
    class OTMLParser {
        +parse()
    }
```

```{mermaid}
:caption: Outfit

classDiagram
    class Outfit {
        +getColor()
        +draw()
        +draw()
        +setId()
        +setAuxId()
        +setHead()
        +setBody()
        +setLegs()
        +setFeet()
        +setAddons()
        +setMount()
        +setWings()
        +setAura()
        +setCategory()
        +setShader()
        +setHealthBar()
        +setManaBar()
        +setCenter()
        +resetClothes()
        +resetShader()
        ... (14 more members)
    }
    class DrawQueueItemOutfit {
    }
    class DrawQueueItemOutfitWithShader {
    }
```

```{mermaid}
:caption: Outputmessage

classDiagram
    class OutputMessage {
        +reset()
        +setBuffer()
        +getBuffer()
        +addU8()
        +addU16()
        +addU32()
        +addU64()
        +addString()
        +addRawString()
        +addPaddingBytes()
        +encryptRsa()
        +getWritePos()
        +getMessageSize()
        +setWritePos()
        +setMessageSize()
        #writeChecksum()
        #writeSequence()
        #writeMessageSize()
    }
```

```{mermaid}
:caption: Packed Any

classDiagram
    class can_pack_in_any {
    }
    class packed_any {
    }
    class placeholder {
    }
    class holder {
    }
```

```{mermaid}
:caption: Packed Storage

classDiagram
    class packed_storage {
    }
    class value_pair {
    }
```

```{mermaid}
:caption: Packet Player

classDiagram
    class PacketPlayer {
    }
```

```{mermaid}
:caption: Packet Recorder

classDiagram
    class PacketRecorder {
    }
```

```{mermaid}
:caption: Painter

classDiagram
    class Painter {
    }
    class PainterState {
    }
```

```{mermaid}
:caption: Paintershaderprogram

classDiagram
    class PainterShaderProgram {
    }
```

```{mermaid}
:caption: Platform

classDiagram
    class Platform {
        +processArgs()
        +spawnProcess()
        +getProcessId()
        +isProcessRunning()
        +killProcess()
        +getTempPath()
        +getCurrentDir()
        +copyFile()
        +fileExists()
        +removeFile()
        +getFileModificationTime()
        +openUrl()
        +openDir()
        +getCPUName()
        +getTotalSystemMemory()
        +getMemoryUsage()
        +getOSName()
        +traceback()
        +getMacAddresses()
        +getUserName()
        ... (3 more members)
    }
```

```{mermaid}
:caption: Platformwindow

classDiagram
    class PlatformWindow {
        +init()
        +terminate()
        +move()
        +resize()
        +show()
        +hide()
        +minimize()
        +maximize()
        +poll()
        +swapBuffers()
        +showMouse()
        +hideMouse()
        +displayFatalError()
        +loadMouseCursor()
        +setMouseCursor()
        +restoreMouseCursor()
        +setTitle()
        +setMinimumSize()
        +setFullscreen()
        +setVerticalSync()
        ... (58 more members)
    }
```

```{mermaid}
:caption: Player

classDiagram
    class Player {
        +asPlayer()
        +isPlayer()
    }
```

```{mermaid}
:caption: Pngunpacker

classDiagram
    class FileMetadata {
        +getOffset()
        +getFileSize()
    }
    class PngUnpacker {
        +unpack()
    }
```

```{mermaid}
:caption: Point

classDiagram
    class TSize {
        +isNull()
        +toSize()
        +operator
        +length()
        +manhattanLength()
        +distanceFrom()
    }
    class TPoint {
        +isNull()
        +toSize()
        +operator
        +length()
        +manhattanLength()
        +distanceFrom()
    }
```

```{mermaid}
:caption: Position

classDiagram
    class Position {
        +translatedToDirection()
        +pos
        +pos
        +translatedToReverseDirection()
        +pos
        +pos
        +translatedToDirections()
        +lastPos
        +positions
        +positions
        +positions
        +getAngleFromPositions()
        +dx
        +dy
        +angle
        +angle
        +getAngleFromPosition()
        +getAngleFromPositions()
        +angle
        +if()
        ... (37 more members)
    }
    class PositionHasher {
    }
```

```{mermaid}
:caption: Protocol

classDiagram
    class Protocol {
        +connect()
        +disconnect()
        +setRecorder()
        +playRecord()
        +isConnected()
        +isConnecting()
        +getElapsedTicksSinceLastRead()
        +getConnection()
        +setConnection()
        +generateXteaKey()
        +setXteaKey()
        +getXteaKey()
        +enableXteaEncryption()
        +enableChecksum()
        +enabledSequencedPackets()
        +enableBigPackets()
        +enableCompression()
        +send()
        +recv()
        +asProtocol()
        ... (11 more members)
    }
```

```{mermaid}
:caption: Protocolgame

classDiagram
    class ProtocolGame {
        +login()
        +send()
        +sendExtendedOpcode()
        +sendLoginPacket()
        +sendWorldName()
        +sendEnterGame()
        +sendLogout()
        +sendPing()
        +sendPingBack()
        +sendNewPing()
        +sendAutoWalk()
        +sendWalkNorth()
        +sendWalkEast()
        +sendWalkSouth()
        +sendWalkWest()
        +sendStop()
        +sendWalkNorthEast()
        +sendWalkSouthEast()
        +sendWalkSouthWest()
        +sendWalkNorthWest()
        ... (97 more members)
    }
```

```{mermaid}
:caption: Proxy

classDiagram
    class ProxyManager {
    }
```

```{mermaid}
:caption: Proxy Client

classDiagram
    class Session {
        +m_io()
        +start()
        +terminate()
        +getPing()
        +getRealPing()
        +getPriority()
        +isConnected()
        +getHost()
        +getPort()
        +getDebugInfo()
        +isActive()
        +addSession()
        +removeSession()
        +send()
    }
    class Proxy {
    }
    class Session {
    }
```

```{mermaid}
:caption: Qrcodegen

classDiagram
    class qrcodegen_Segment {
    }
    class qrcodegen_Segment {
    }
    class qrcodegen_Segment {
    }
    class qrcodegen_Segment {
    }
    class qrcodegen_Segment {
    }
```

```{mermaid}
:caption: Rect

classDiagram
    class TPoint {
        +isNull()
        +isEmpty()
        +isValid()
        +left()
        +top()
        +right()
        +bottom()
        +horizontalCenter()
        +verticalCenter()
        +x()
        +y()
        +topLeft()
        +bottomRight()
        +topRight()
        +bottomLeft()
        +topCenter()
        +bottomCenter()
        +centerLeft()
        +centerRight()
        +center()
        ... (102 more members)
    }
    class TSize {
        +isNull()
        +isEmpty()
        +isValid()
        +left()
        +top()
        +right()
        +bottom()
        +horizontalCenter()
        +verticalCenter()
        +x()
        +y()
        +topLeft()
        +bottomRight()
        +topRight()
        +bottomLeft()
        +topCenter()
        +bottomCenter()
        +centerLeft()
        +centerRight()
        +center()
        ... (102 more members)
    }
    class TRect {
        +isNull()
        +isEmpty()
        +isValid()
        +left()
        +top()
        +right()
        +bottom()
        +horizontalCenter()
        +verticalCenter()
        +x()
        +y()
        +topLeft()
        +bottomRight()
        +topRight()
        +bottomLeft()
        +topCenter()
        +bottomCenter()
        +centerLeft()
        +centerRight()
        +center()
        ... (102 more members)
    }
```

```{mermaid}
:caption: Resourcemanager

classDiagram
    class ResourceManager {
        +init()
        +terminate()
        +launchCorrect()
        +setupWriteDir()
        +setup()
        +getCompactName()
        +loadDataFromSelf()
        +fileExists()
        +directoryExists()
        +readFileStream()
        +readFileContents()
        +readFileContentsSafe()
        +isFileEncryptedOrCompressed()
        +writeFileBuffer()
        +writeFileContents()
        +writeFileStream()
        +openFile()
        +appendFile()
        +createFile()
        +deleteFile()
        ... (28 more members)
    }
```

```{mermaid}
:caption: Result

classDiagram
    class HttpSession {
    }
    class HttpResult {
    }
```

```{mermaid}
:caption: Scheduledevent

classDiagram
    class ScheduledEvent {
        +execute()
        +nextCycle()
        +ticks()
        +remainingTicks()
        +delay()
        +cyclesExecuted()
        +maxCycles()
    }
    class lessScheduledEvent {
    }
```

```{mermaid}
:caption: Sdlwindow

classDiagram
    class SDLWindow {
    }
```

```{mermaid}
:caption: Server

classDiagram
    class Server {
        +create()
        +isOpen()
        +close()
        +acceptNext()
    }
```

```{mermaid}
:caption: Session

classDiagram
    class HttpSession {
        +start()
        +cancel()
    }
```

```{mermaid}
:caption: Shader

classDiagram
    class Shader {
        +compileSourceCode()
        +compileSourceFile()
        +log()
        +getShaderId()
        +getShaderType()
    }
```

```{mermaid}
:caption: Shadermanager

classDiagram
    class ShaderManager {
        +init()
        +terminate()
        +createShader()
        +createOutfitShader()
        +createShader()
        +addTexture()
        +getShader()
    }
```

```{mermaid}
:caption: Shaderprogram

classDiagram
    class ShaderProgram {
    }
```

```{mermaid}
:caption: Shared Object

classDiagram
    class shared_object_ptr {
        +add_ref()
        +dec_ref()
        +ref_count()
    }
    class shared_object {
        +add_ref()
        +dec_ref()
        +ref_count()
    }
    class shared_object_ptr {
        +reset()
        +reset()
        +swap()
        +use_count()
        +is_unique()
        +unspecified_bool_type()
    }
```

```{mermaid}
:caption: Size

classDiagram
    class TSize {
        +toPoint()
        +isNull()
        +isEmpty()
        +isValid()
        +width()
        +height()
        +resize()
        +setWidth()
        +setHeight()
        +operator
        +expandedTo()
        +boundedTo()
        +scale()
        +useHeight
        +rw
        +scale()
        +ratio()
        +area()
    }
```

```{mermaid}
:caption: Soundbuffer

classDiagram
    class SoundBuffer {
        +fillBuffer()
        +fillBuffer()
        +getBufferId()
    }
```

```{mermaid}
:caption: Soundchannel

classDiagram
    class SoundChannel {
        +play()
        +stop()
        +enqueue()
        +enable()
        +disable()
        +setGain()
        +getGain()
        +setEnabled()
        +isEnabled()
        +getId()
        #update()
    }
    class QueueEntry {
    }
```

```{mermaid}
:caption: Soundfile

classDiagram
    class SoundFile {
        +loadSoundFile()
        +read()
        +reset()
        +eof()
        +getSampleFormat()
        +getChannels()
        +getRate()
        +getBps()
        +getSize()
        +getName()
        #m_file
        #m_channels
        #m_rate
        #m_bps
        #m_size
    }
```

```{mermaid}
:caption: Soundmanager

classDiagram
    class SoundManager {
        +init()
        +terminate()
        +poll()
        +setAudioEnabled()
        +isAudioEnabled()
        +enableAudio()
        +disableAudio()
        +stopAll()
        +preload()
        +play()
        +getChannel()
        +resolveSoundFile()
        +ensureContext()
    }
```

```{mermaid}
:caption: Soundsource

classDiagram
    class SoundSource {
        +play()
        +stop()
        +isBuffering()
        +isPlaying()
        +setName()
        +setLooping()
        +setRelative()
        +setReferenceDistance()
        +setGain()
        +setPitch()
        +setPosition()
        +setVelocity()
        +setFading()
        +getName()
        +getChannel()
        +getGain()
        #setBuffer()
        #setChannel()
        #update()
        #m_sourceId
        ... (8 more members)
    }
```

```{mermaid}
:caption: Spritemanager

classDiagram
    class SpriteManager {
        +terminate()
        +loadSpr()
        +unload()
        +saveSpr()
        +saveSpr64()
        +encryptSprites()
        +dumpSprites()
        +getSignature()
        +getSpritesCount()
        +getSpriteImage()
        +isLoaded()
        +spriteSize()
        +getOffsetFactor()
        +isHdMod()
    }
```

```{mermaid}
:caption: Statictext

classDiagram
    class StaticTextMessage {
    }
    class StaticText {
        +drawText()
        +getName()
        +getText()
        +getMessageMode()
        +getFirstMessage()
        +isYell()
        +setText()
        +setFont()
        +addMessage()
        +addColoredMessage()
        +asStaticText()
        +isStaticText()
        +setColor()
        +getColor()
        +hasText()
    }
```

```{mermaid}
:caption: Stats

classDiagram
    class Stat {
    }
    class StatsData {
    }
    class UIWidget {
        +add()
        +get()
        +clear()
        +clearAll()
        +getSlow()
        +clearSlow()
        +types()
        +getSleepTime()
        +m_sleepTime
        +resetSleepTime()
        +m_sleepTime
        +addWidget()
        +removeWidget()
        +getWidgetsInfo()
        +addTexture()
        +removeTexture()
        +addThing()
        +removeThing()
        +addCreature()
        +removeCreature()
    }
    class Stats {
    }
    class AutoStat {
    }
```

```{mermaid}
:caption: Streamsoundsource

classDiagram
    class StreamSoundSource {
        +play()
        +stop()
        +isPlaying()
        +setSoundFile()
        +downMix()
        +update()
    }
```

```{mermaid}
:caption: Textrender

classDiagram
    class TextRenderCache {
    }
    class TextRender {
        +init()
        +terminate()
        +poll()
        +addText()
        +drawText()
        +drawText()
        +drawColoredText()
    }
```

```{mermaid}
:caption: Texture

classDiagram
    class Texture {
        +replace()
        +resize()
        +update()
        +setUpsideDown()
        +setSmooth()
        +setRepeat()
        +buildHardwareMipmaps()
        +setTime()
        +setCanCache()
        +getId()
        +getUniqueId()
        +getTime()
        +getWidth()
        +getHeight()
        +isEmpty()
        +hasRepeat()
        +hasMipmaps()
        +canCache()
        +isAnimatedTexture()
        #uploadPixels()
        ... (18 more members)
    }
```

```{mermaid}
:caption: Texturemanager

classDiagram
    class TextureManager {
        +init()
        +terminate()
        +clearCache()
        +reload()
        +preload()
        +getTexture()
        +loadTexture()
    }
```

```{mermaid}
:caption: Thing

classDiagram
    class Thing {
        +draw()
        +setId()
        +setPosition()
        +getId()
        +getPosition()
        +getStackPriority()
        +getParentContainer()
        +getStackPos()
        +setMarked()
        +updatedMarkedColor()
        +isItem()
        +isEffect()
        +isMissile()
        +isCreature()
        +isNpc()
        +isMonster()
        +isPlayer()
        +isLocalPlayer()
        +isAnimatedText()
        +isStaticText()
        ... (73 more members)
    }
```

```{mermaid}
:caption: Thingstype

classDiagram
    class ThingsType {
        +load()
        +unload()
        +parseThingType()
        +getSignature()
        +isLoaded()
        +getFirstItemId()
        +getMaxItemid()
        +isValidItemId()
    }
```

```{mermaid}
:caption: Thingtype

classDiagram
    class MarketData {
    }
    class StoreCategory {
    }
    class StoreOffer {
    }
    class Imbuement {
    }
    class Light {
    }
    class DrawOutfitParams {
    }
    class ThingType {
        +unserialize()
        +unserializeOtml()
        +unload()
        +serialize()
        +exportImage()
        +replaceSprites()
        +drawOutfit()
        +getDrawSize()
        +drawWithShader()
        +drawWithShader()
        +getId()
        +getCategory()
        +isNull()
        +hasAttr()
        +isLoaded()
        +getLastUsage()
        +getSize()
        +getWidth()
        +getHeight()
        +getExactSize()
        ... (63 more members)
    }
    class DrawQueueItemThingWithShader {
    }
```

```{mermaid}
:caption: Thingtypemanager

classDiagram
    class ThingTypeManager {
        +init()
        +terminate()
        +check()
        +loadDat()
        +loadOtml()
        +loadOtb()
        +loadXml()
        +parseItemType()
        +saveDat()
        +dumpTextures()
        +replaceTextures()
        +addItemType()
        +findItemTypesByName()
        +findItemTypesByString()
        +getMarketCategories()
        +m_marketCategories
        +findThingTypeByAttr()
        +findItemTypeByCategory()
        +getDatSignature()
        +getOtbMajorVersion()
        ... (7 more members)
    }
```

```{mermaid}
:caption: Tile

classDiagram
    class Tile {
        +calculateCorpseCorrection()
        +drawGround()
        +drawBottom()
        +drawCreatures()
        +drawTop()
        +drawTexts()
        +drawWidget()
        +clean()
        +addWalkingCreature()
        +removeWalkingCreature()
        +addThing()
        +removeThing()
        +getThing()
        +getEffect()
        +hasThing()
        +getThingStackPos()
        +getTopThing()
        +getTopLookThing()
        +getTopLookThingEx()
        +getTopUseThing()
        ... (59 more members)
    }
```

```{mermaid}
:caption: Time

classDiagram
    class timer {
    }
```

```{mermaid}
:caption: Timer

classDiagram
    class Timer {
        +restart()
        +stop()
        +adjust()
        +startTicks()
        +ticksElapsed()
        +timeElapsed()
        +running()
    }
```

```{mermaid}
:caption: Tinystr

classDiagram
    class TiXmlString {
    }
    class Rep {
    }
    class TiXmlOutStream {
    }
```

```{mermaid}
:caption: Towns

classDiagram
    class Town {
        +setId()
        +setName()
        +setPos()
        +getId()
        +getName()
        +getPos()
    }
    class TownManager {
        +addTown()
        +removeTown()
        +sort()
        +getTowns()
        +clear()
        #findTown()
    }
```

```{mermaid}
:caption: Uianchorlayout

classDiagram
    class UIAnchor {
        +getAnchoredEdge()
        +getHookedEdge()
        +getHookedWidget()
        +getHookedPoint()
        #m_anchoredEdge
        #m_hookedEdge
        #m_hookedWidgetId
    }
    class UIAnchorGroup {
        +addAnchor()
        +isUpdated()
        +setUpdated()
    }
    class UIAnchorLayout {
        +removeAnchors()
        +hasAnchors()
        +centerIn()
        +fill()
        +addWidget()
        +removeWidget()
        +isUIAnchorLayout()
        #internalUpdate()
        #updateWidget()
        #m_anchorsGroups
    }
```

```{mermaid}
:caption: Uiboxlayout

classDiagram
    class UIBoxLayout {
        +applyStyle()
        +addWidget()
        +removeWidget()
        +setSpacing()
        +setFitChildren()
        +isUIBoxLayout()
        #m_fitChildren
        #m_spacing
    }
```

```{mermaid}
:caption: Uicreature

classDiagram
    class UICreature {
        +drawSelf()
        +setCreature()
        +setFixedCreatureSize()
        +setOutfit()
        +getCreature()
        +getOutfit()
        +isFixedCreatureSize()
        +setAutoRotating()
        +setDirection()
        +getDirection()
        +setScale()
        +getScale()
        +setAnimate()
        +isAnimating()
        +setCenter()
        +setOldScaling()
        #onStyleApply()
        #onGeometryChange()
        #m_creature
        #m_autoRotating
        ... (4 more members)
    }
```

```{mermaid}
:caption: Uigraph

classDiagram
    class UIGraph {
    }
```

```{mermaid}
:caption: Uigridlayout

classDiagram
    class UIGridLayout {
        +applyStyle()
        +removeWidget()
        +addWidget()
        +setCellSize()
        +setCellWidth()
        +setCellHeight()
        +setCellSpacing()
        +setNumColumns()
        +setNumLines()
        +setAutoSpacing()
        +setFitChildren()
        +setFlow()
        +getCellSize()
        +getCellSpacing()
        +getNumColumns()
        +getNumLines()
        +isUIGridLayout()
        #internalUpdate()
    }
```

```{mermaid}
:caption: Uihorizontallayout

classDiagram
    class UIHorizontalLayout {
        +applyStyle()
        +setAlignRight()
        +isUIHorizontalLayout()
        #internalUpdate()
        #m_alignChidren
        #m_alignRight
    }
```

```{mermaid}
:caption: Uiitem

classDiagram
    class UIItem {
        +drawSelf()
        +setItemId()
        +setItemCount()
        +setItemSubType()
        +setItemVisible()
        +setItem()
        +setVirtual()
        +clearItem()
        +setShowCount()
        +setItemShader()
        +getItemId()
        +getItemCount()
        +getItemSubType()
        +getItemCountOrSubType()
        +getItem()
        +isVirtual()
        +isItemVisible()
        #onStyleApply()
        #cacheCountText()
        #m_item
        ... (6 more members)
    }
```

```{mermaid}
:caption: Uilayout

classDiagram
    class UILayout {
        +update()
        +updateLater()
        +applyStyle()
        +addWidget()
        +removeWidget()
        +disableUpdates()
        +enableUpdates()
        +setParent()
        +getParentWidget()
        +isUpdateDisabled()
        +isUpdating()
        +isUIAnchorLayout()
        +isUIBoxLayout()
        +isUIHorizontalLayout()
        +isUIVerticalLayout()
        +isUIGridLayout()
        #internalUpdate()
        #m_updateDisabled
        #m_updating
        #m_updateScheduled
        ... (1 more members)
    }
```

```{mermaid}
:caption: Uimanager

classDiagram
    class UIManager {
        +init()
        +terminate()
        +render()
        +resize()
        +inputEvent()
        +updatePressedWidget()
        +updateDraggingWidget()
        +updateHoveredWidget()
        +clearStyles()
        +importStyle()
        +importStyleFromString()
        +importStyleFromOTML()
        +getStyle()
        +getStyleClass()
        +loadUIFromString()
        +loadUI()
        +displayUI()
        +createWidget()
        +createWidgetFromOTML()
        +setMouseReceiver()
        ... (16 more members)
    }
```

```{mermaid}
:caption: Uimap

classDiagram
    class UIMap {
        +onMouseMove()
        +drawSelf()
        +movePixels()
        +setZoom()
        +zoomIn()
        +zoomOut()
        +followCreature()
        +setCameraPosition()
        +setMaxZoomIn()
        +setMaxZoomOut()
        +setMultifloor()
        +lockVisibleFloor()
        +unlockVisibleFloor()
        +setVisibleDimension()
        +setDrawFlags()
        +setDrawTexts()
        +setDrawNames()
        +setDrawHealthBars()
        +setDrawHealthBarsOnTop()
        +setDrawLights()
        ... (34 more members)
    }
```

```{mermaid}
:caption: Uimapanchorlayout

classDiagram
    class UIPositionAnchor {
        +getHookedWidget()
        +getHookedPoint()
    }
    class UIMapAnchorLayout {
        +centerInPosition()
        +fillPosition()
    }
```

```{mermaid}
:caption: Uiminimap

classDiagram
    class UIMinimap {
        +drawSelf()
        +zoomIn()
        +zoomOut()
        +setZoom()
        +setMinZoom()
        +setMaxZoom()
        +setCameraPosition()
        +floorUp()
        +floorDown()
        +getTilePoint()
        +getTileRect()
        +getTilePosition()
        +getCameraPosition()
        +getMinZoom()
        +getMaxZoom()
        +getZoom()
        +getScale()
        +anchorPosition()
        +fillPosition()
        +centerInPosition()
        ... (3 more members)
    }
```

```{mermaid}
:caption: Uiprogressrect

classDiagram
    class UIProgressRect {
        +drawSelf()
        +setPercent()
        +getPercent()
        #onStyleApply()
        #m_percent
    }
```

```{mermaid}
:caption: Uisprite

classDiagram
    class UISprite {
        +drawSelf()
        +setSpriteId()
        +getSpriteId()
        +clearSprite()
        +setSpriteColor()
        +isSpriteVisible()
        +setSpriteVisible()
        +hasSprite()
        #onStyleApply()
        #m_sprite
        #m_spriteId
        #m_spriteColor
        #m_spriteVisible
    }
```

```{mermaid}
:caption: Uitextedit

classDiagram
    class UITextEdit {
        +drawSelf()
        +setCursorPos()
        +setSelection()
        +setCursorVisible()
        +setTextHidden()
        +setValidCharacters()
        +setShiftNavigation()
        +setMultiline()
        +setMaxLength()
        +setTextVirtualOffset()
        +setEditable()
        +setSelectable()
        +setSelectionColor()
        +setSelectionBackgroundColor()
        +setAutoScroll()
        +setAutoSubmit()
        +setPlaceholder()
        +setPlaceholderColor()
        +setPlaceholderAlign()
        +setPlaceholderFont()
        ... (44 more members)
    }
```

```{mermaid}
:caption: Uiverticallayout

classDiagram
    class UIVerticalLayout {
        +applyStyle()
        +setAlignBottom()
        +isAlignBottom()
        +isUIVerticalLayout()
        #internalUpdate()
        #m_alignBottom
    }
```

```{mermaid}
:caption: Uiwidget

classDiagram
    class EdgeGroup {
    }
    class UIWidget {
        +draw()
        #drawSelf()
        #drawChildren()
        #m_id
        #m_source
        #m_rect
        #m_virtualOffset
        #m_autoDraw
        #m_enabled
        #m_visible
        #m_focusable
        #m_fixedSize
        #m_phantom
        #m_draggable
        #m_destroyed
        #m_clipping
        #m_layout
        #m_parent
        #m_parentId
        #m_children
        ... (374 more members)
    }
```

```{mermaid}
:caption: Uri

classDiagram
    class ParsedURI {
    }
```

```{mermaid}
:caption: Vertexarray

classDiagram
    class VertexArray {
        +m_hardwareBuffer
        +addVertex()
        +addTriangle()
        +addRect()
        +top
        +right
        +bottom
        +left
        +addRect()
        +top
        +right
        +bottom
        +left
        +addQuad()
        +top
        +right
        +bottom
        +left
        +addUpsideDownQuad()
        +top
        ... (8 more members)
    }
```

```{mermaid}
:caption: Walkmatrix

classDiagram
    class WalkMatrix {
    }
```

```{mermaid}
:caption: Websocket

classDiagram
    class WebsocketSession {
        +start()
        +send()
        +close()
    }
```

```{mermaid}
:caption: Win32Window

classDiagram
    class WindowProcProxy {
        +init()
        +terminate()
        +move()
        +resize()
        +show()
        +hide()
        +minimize()
        +maximize()
        +poll()
        +swapBuffers()
        +showMouse()
        +hideMouse()
        +displayFatalError()
        +setMouseCursor()
        +restoreMouseCursor()
        +setTitle()
        +setMinimumSize()
        +setFullscreen()
        +setVerticalSync()
        +setIcon()
        ... (6 more members)
    }
    class WIN32Window {
        +init()
        +terminate()
        +move()
        +resize()
        +show()
        +hide()
        +minimize()
        +maximize()
        +poll()
        +swapBuffers()
        +showMouse()
        +hideMouse()
        +displayFatalError()
        +setMouseCursor()
        +restoreMouseCursor()
        +setTitle()
        +setMinimumSize()
        +setFullscreen()
        +setVerticalSync()
        +setIcon()
        ... (6 more members)
    }
```

```{mermaid}
:caption: X11Window

classDiagram
    class X11Window {
        +init()
        +terminate()
        +move()
        +resize()
        +show()
        +hide()
        +minimize()
        +maximize()
        +poll()
        +swapBuffers()
        +showMouse()
        +hideMouse()
        +setMouseCursor()
        +restoreMouseCursor()
        +setTitle()
        +setMinimumSize()
        +setFullscreen()
        +setVerticalSync()
        +setIcon()
        +setClipboardText()
        ... (5 more members)
    }
```
