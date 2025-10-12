# src/client/animator.h

```cpp
public:
    Animator();
```
```cpp
void unserialize(int animationPhases, const FileStreamPtr& fin);
```
```cpp
void serialize(const FileStreamPtr& fin);
```
```cpp
void setPhase(int phase);
```
```cpp
int getPhase();
```
```cpp
int getPhaseAt(Timer& timer, int lastPhase = 0);
```
```cpp
int getStartPhase();
```
```cpp
int getAnimationPhases() { return m_animationPhases; } bool isAsync() { return m_async; } bool isComplete() { return m_isComplete; } ticks_t getTotalDuration();
```
```cpp
void resetAnimation();
```
```cpp
private:
    int getPingPongPhase();
```
```cpp
int getLoopPhase();
```
```cpp
int getPhaseDuration(int phase);
```
```cpp
void calculateSynchronous();
```