# T22 Optimization Quick Reference

## Skill ID Mapping (Old → New)

### Skills That Changed IDs

| Original ID | New ID(s) | Change Type | Notes |
|------------|-----------|-------------|-------|
| T22.G5.04 | **REMOVED** | Duplicate removed | Was duplicate of T22.G3.02; references updated to T22.G5.03 |
| T22.G6.03 | T22.G6.03.01<br>T22.G6.03.02 | Split into 2 | .01 = streaming mode<br>.02 = cancel request |
| T22.G7.06 | T22.G7.06.01<br>T22.G7.06.02<br>T22.G7.06.03 | Split into 3 | .01 = attach costume<br>.02 = attach files<br>.03 = attach Google Drive |
| T22.G7.07 | T22.G7.07.01<br>T22.G7.07.02 | Split into 2 | .01 = image URL moderation<br>.02 = costume moderation |
| T22.G7.08 | T22.G7.08.01<br>T22.G7.08.02 | Split into 2 | .01 = LLM request block<br>.02 = LLM system instruction |

### Skills With Updated Dependencies

All skills that previously referenced changed IDs have been updated:

#### References to T22.G5.04 (removed)
- Updated to reference T22.G5.03 instead

#### References to T22.G6.03 (split)
Skills now reference **T22.G6.03.01** (streaming mode):
- T22.G6.04.02: Build a conversation log with dynamic updates
- T22.G6.05: Implement session management for multi-turn conversations
- T22.G6.06.01: Create and configure a pre-built chat window
- T22.G6.06.02: Manage chat messages with append and update blocks
- T22.G6.06.03: Display streaming responses in real-time with update block
- T22.G7.01: Use system messages to set bot behavior
- T22.G7.02.01: Create and use custom personas with system messages
- T22.G7.02.02: Use few-shot prompting with example exchanges

#### References to T22.G7.06 (split into 3)
Skills reference specific attachment sub-skills:
- T22.G7.07.01 depends on T22.G7.06.02 (local files)
- T22.G7.07.02 depends on T22.G7.06.01 (costumes)

## Block-to-Skill Mapping

### Main ChatGPT Blocks
| Block | Primary Skill(s) |
|-------|------------------|
| `OpenAI ChatGPT: request [PROMPT] result [VARIABLE]` | T22.G3.02, T22.G6.01.01, T22.G6.01.02 |
| `OpenAI ChatGPT: system request [PROMPT]` | T22.G7.01 |
| `OpenAI ChatGPT: cancel request` | T22.G6.03.02 |
| `select ChatGPT bot [1/2/3/4]` | T22.G6.08, T22.G8.02 |

### Chat Window Blocks
| Block | Primary Skill(s) |
|-------|------------------|
| `add chat window x (X) y (Y) width (WIDTH)...` | T22.G6.06.01 |
| `append to chat [CHATNAME] message [MESSAGE]...` | T22.G6.06.02 |
| `update last chat message to [MESSAGE]...` | T22.G6.06.03 |

### File Attachment Blocks
| Block | Primary Skill(s) |
|-------|------------------|
| `attach costume [COSTUMENAME] to chat` | T22.G7.06.01 |
| `attach files to chat` | T22.G7.06.02 |
| `attach file from Google Drive [URL] to chat` | T22.G7.06.03 |

### Moderation Blocks
| Block | Primary Skill(s) |
|-------|------------------|
| `get moderation result for [TEXT]` | T22.G7.05 |
| `get moderation result for image at URL [URL]` | T22.G7.07.01 |
| `get moderation result for costume named [NAME]` | T22.G7.07.02 |

### Generic LLM Blocks
| Block | Primary Skill(s) |
|-------|------------------|
| `LLM model [PROVIDER] request [PROMPT]...` | T22.G7.08.01 |
| `LLM set system instruction [INSTRUCTION] for model [PROVIDER]` | T22.G7.08.02 |

### Semantic Search/RAG Blocks
| Block | Primary Skill(s) |
|-------|------------------|
| `create semantic database from table [TABLE]` | T22.G8.01.01 |
| `search semantic database with [QUERY]...` | T22.G8.01.02 |

### Web Search Blocks
| Block | Primary Skill(s) |
|-------|------------------|
| `web search [QUERY] store top (K) in table [TABLE]` | T22.G8.05 |

## Structural Fixes

### Separator Placement
- **Before**: Separators sometimes appeared in wrong locations, including within dependency lists
- **After**: Separators only between grade levels (after GK, G1, G2, G3, G4, G5, G6, G7)

### Dependency Format
- **Before**: Some missing descriptions, inconsistent format
- **After**: All use format `* T##.G#.##: [Full skill description]`

## Quick Stats

| Metric | Count |
|--------|-------|
| Total skills in optimized T22 | 47 |
| Skills removed (duplicates) | 1 |
| Skills split into sub-skills | 4 |
| New sub-skills created | 10 |
| Skills with simplified dependencies | ~15 |
| Cross-topic dependencies preserved | All (T06-T29) |

## Grade Level Distribution

```
K:  2 skills (unplugged/picture-based)
1:  2 skills (unplugged/picture-based)
2:  2 skills (unplugged/picture-based)
3:  3 skills (intro to ChatGPT blocks)
4:  3 skills (basic Q&A chatbots)
5:  4 skills (testing & prompting)
6: 13 skills (parameters, UI, sessions)
7: 13 skills (system messages, personas, attachments, LLMs)
8:  5 skills (RAG, multi-agent, JSON, testing, web search)
```

## Key Concepts by Grade

### Grade 3: First Exposure
- Recognizing chatbot behavior vs fixed responses
- Basic request/response with ChatGPT block
- Displaying AI responses

### Grade 4: Basic Interaction
- Writing effective prompts
- Building Q&A interfaces
- Testing with different questions

### Grade 5: Understanding & Testing
- Safety and responsible use
- Observing strengths/weaknesses
- Experimenting with phrasing
- Understanding parameters (conceptually)

### Grade 6: Configuration & UI
- Parameter adjustment (temperature, tokens, mode)
- Streaming vs. waiting modes
- Request cancellation
- Building conversation interfaces (custom or pre-built)
- Session management
- Multiple chatbot sessions

### Grade 7: Advanced Prompting & Multimodal
- System messages
- Custom personas
- Few-shot prompting
- Chat history management
- UI widget integration
- Moderation guardrails
- File/image attachments (3 types)
- Image moderation (2 types)
- Generic LLM models (2 skills)
- User testing for inclusivity

### Grade 8: Professional Techniques
- Semantic search & RAG (3 skills)
- Multi-agent conversations
- Structured output/JSON (3 skills)
- Automated testing
- Web search integration

## Common Dependency Patterns

### Core T22 Progression
```
G3: Basic request → Display response
G4: Write prompts → Build Q&A → Handle variety
G5: Safety → Observe → Experiment → Understand params
G6: Configure params → Build UI → Manage sessions
G7: System messages → Personas → Advanced features
G8: Professional integration patterns
```

### Cross-Topic Foundations
- **T06 (Events)**: Required for multi-script coordination
- **T07 (Loops)**: Required for repeated interactions
- **T08 (Conditionals)**: Required for logic/moderation
- **T09 (Variables)**: Required for data management
- **T10 (Tables)**: Required for RAG/search features
- **T16 (UI Widgets)**: Required for chat interfaces
- **T21 (AI Safety)**: Required for moderation skills

## Integration Notes

When integrating this optimized T22 into allskills.md:

1. **Search for**: `ID: T22.GK.01` to locate T22 section
2. **Replace entire T22 section** (through end of T22.G8.05) with optimized version
3. **Verify separator placement**: Should have `---` after each grade level except G8
4. **Check cross-references**: If other topics reference old T22 IDs, update them:
   - T22.G5.04 → T22.G5.03 (if any exist)
   - T22.G6.03 → T22.G6.03.01
   - T22.G7.06 → T22.G7.06.01/.02/.03 (as appropriate)
   - T22.G7.07 → T22.G7.07.01/.02 (as appropriate)
   - T22.G7.08 → T22.G7.08.01/.02 (as appropriate)

## Validation Checklist

- [ ] All skills focus on ONE block/concept
- [ ] All dependencies properly formatted with descriptions
- [ ] No dependencies after separators
- [ ] Separators only between grade levels
- [ ] X-2 rule followed (grade X depends on X, X-1, X-2 only)
- [ ] K-2 skills are unplugged/picture-based
- [ ] G3+ skills use block-based coding
- [ ] All cross-topic dependencies preserved
- [ ] Sub-skill numbering consistent (T##.G#.##.##)
- [ ] Progressive complexity maintained
