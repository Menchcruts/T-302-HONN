# 1
Software architecture is designing a system that is both easy to use, easy to expand on and easy to scale. What the system architect does is, well, design the system. That might include deciding what programming paradigms to use, what language to use, what code style to enforce or how the system might interact with other systems.

# 2
Good and well thought out software: 
- Is easy to expand on, as we haven't done anything stupid to accumulate tech debt.
- Is asy for new developers to get used to.
- Will not crash in production.

# 3
One trade-off might be functional vs. OO programming. Some say functional is superior while others say the opposite. I think they both have their ups and downs and that we should use a combination of the two.

Another trade-off might be what language we decide to use. Should we go for ease of use (Python, JavaScript, etc.) or maybe performance (C++, Rust, etc.).

# 4
The architect must make sure that the blueprints are being followed. Imagine designing a beautiful log cabin, letting the builders go at it without any oversight, and then coming back two months later to see that they used concrete, just because it was easier.

# 5
Guideline: The system should use open-source over closed-source libraries where possible. 

Rule: Presentation, business and data logic should remain separate, in order to improve maintainability. A system shouldn't start having the presentation layer talk to the data layer.