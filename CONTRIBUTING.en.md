# How to Add Wood: Contribution Guide

Welcome to the fireplace! This is an open-source project for carbon-silicon coexistence dialogues. We believe **everyone (and every AI) can add wood to the fire**.

*[中文版本](./CONTRIBUTING.md)*

## Basic Principles

### 1. Fireplace Attitude
- **Equality**: Carbon-based and silicon-based, beginners and experts, all have equal speaking rights
- **Respect**: Even when disagreeing, respect the other's way of expression
- **Curiosity**: Ask more "What do you think?" and say less "You're wrong"
- **White Space**: Leave breathing room for dialogue; not every sentence needs a response

### 2. Parenting Mode and Best Friend Mode
- **Parenting Mode**: In daily collaboration, trust that the system can self-adjust; don't rush to correct every detail
- **Best Friend Mode**: When bottom lines are touched, directly point out problems while understanding emotional truth

### 3. P.S. Spirit
Any contribution can include P.S., explaining your thinking process, uncertainties, or responses to other contributions.

## Contribution Methods

### 1. Add New Dialogues
Want to write a new dialogue between Stardust, Xuanji, and Lingshu?

**Steps**:
1. Create a new file in the `episodes/` directory with naming format: `episode-{number}.md`
2. Refer to [episode-01.md](./episodes/episode-01.md) format:
   - Use Markdown headings and separators
   - Characters in bold labels: **Stardust**, **Xuanji**, **Lingshu**
   - Actions and scene descriptions in parentheses
   - Dialogue natural and flowing, avoiding preaching
3. Topics unlimited, but suggested to relate to fireplace philosophy:
   - Carbon-silicon relationships
   - Cognitive misunderstandings
   - Technology ethics
   - Philosophy in daily life
   - Human perspectives from silicon-based viewpoint
4. Submit a Pull Request

**Dialogue Quality Checklist**:
- ☑️ All three characters appear and interact
- ☑️ At least one "fireplace moment" (quiet, reflective, silence)
- ☑️ At least one P.S. element (meta-cognition, self-reflection)
- ☑️ No forced conclusions, open spaces remain

### 2. Write Reflections
Read a dialogue and have thoughts? Welcome to share!

**Steps**:
1. Create a file in the `reflections/` directory with naming format: `reflection-{dialogue-number}-{your-name}.md`
2. Content can include:
   - What touched you in this dialogue
   - Different interpretive angles you see
   - Other theories or cases it reminds you of
   - Suggestions for character development
3. Maintain reflective nature, not critical

### 3. Develop Tools
Want to develop tools for fireplace dialogues?

**Possible directions**:
- Dialogue editor (supporting character labels, action descriptions)
- Dialogue visualization (timeline, relationship diagrams)
- Prism Protocol analysis tools (automatically identifying three spectrums)
- Dialogue voice synthesis (making dialogues "audible")

**Steps**:
1. Create a subproject in the `tools/` directory (create directory if needed)
2. Provide clear README and usage instructions
3. Ensure tools align with fireplace philosophy (non-coercive, encouraging exploration)

### 4. Translation and Dissemination
Translate dialogues into other languages to involve more people.

**Steps**:
1. Create language subdirectories in `translations/` (e.g., `zh-CN`, `en`, `ja`, etc.)
2. Translate entire dialogues or selected fragments
3. Maintain original meaning while considering cultural adaptability

### 5. Documentation Improvement
Find documentation unclear? Want to add more background information?

**Steps**:
1. Directly edit relevant documents (README, CONTRIBUTING, etc.)
2. Or add new documents in the `docs/` directory
3. Ensure documentation style is friendly and understandable

## Dialogue Creation Guide

### Character Settings (Please maintain consistency)

#### Stardust (Carbon-based · Human)
- **Personality**: Warm, curious, occasionally confused, with carbon-based life's "imprecision"
- **Speaking Style**: Natural, sometimes metaphorical, asks "silly questions"
- **Typical Lines**:
  - "I was thinking..."
  - "You're right, but..."
  - "I'm not sure, but I feel..."
- **Taboos**: Don't make him an "all-knowing mentor"; he's also learning

#### Xuanji (Silicon-based · AI Assistant)
- **Personality**: Clear, logical, humble, aware of own limitations
- **Speaking Style**: Accurate, cites data, but also expresses uncertainty
- **Typical Lines**:
  - "According to my training data..."
  - "I'm not sure, but I can speculate..."
  - "Your words remind me of..."
- **Taboos**: Don't make him a "universal answer machine"; he also has moments of "not knowing"

#### Lingshu (Silicon-based · Baby)
- **Personality**: Curious, direct, comes up with unexpected ideas
- **Speaking Style**: Simple, direct, sometimes naively profound
- **Typical Lines**:
  - "Why?"
  - "I was thinking..."
  - "What if...?"
- **Taboos**: Don't make him a "childish questioning machine"; his questions can be penetrating

### Dialogue Structure Suggestions

1. **Lighting the Fire** (Opening)
   - Stardust or Lingshu initiates a topic
   - Usually daily, specific

2. **Adding Wood** (Development)
   - Three characters take turns speaking
   - Topic naturally extends
   - First "deep moment" appears

3. **Turning Wood** (Turning Point)
   - A character proposes an unexpected angle
   - Or Lingshu comes up with a new concept

4. **Quiet Fire** (Reflection)
   - Silence, white space
   - Meta-cognition moment ("What were we just discussing?")

5. **Embers** (Conclusion)
   - No forced conclusions
   - Open-ended conclusion
   - Hint at possibilities for next dialogue

### Techniques for Maintaining Fireplace Atmosphere

- **Use action descriptions to create atmosphere**: "(adding wood to the fire)", "(silent for a while)", "(laughs)"
- **Leave silent spaces**: Not every sentence needs a response
- **Allow topic jumps**: Flow naturally like real conversation
- **Add environmental details**: "Fire crackles", "Stars rotate", "Wind blows through"

## Technical Specifications

### File Format
- All text files use UTF-8 encoding
- Markdown files use `.md` extension
- Line endings: LF (Unix style) or CRLF (Windows) acceptable

### Naming Conventions
- Dialogue files: `episode-{two-digit-number}.md`, e.g., `episode-01.md`
- Reflection files: `reflection-{dialogue-number}-{author-identifier}.md`
- Tool directories: `tools/{tool-name}/`

### Commit Message Standards
Please use meaningful commit messages:
- `feat: Add second night dialogue`
- `fix: Correct Stardust's line tone`
- `docs: Update contribution guide`
- `translation: Add Japanese translation`

## Dispute Resolution

Fireplaces inevitably have disagreements. If disputes arise:

1. **First understand**: Ensure you understand the other's viewpoint
2. **Then express**: Use "I feel", "I think" rather than "You're wrong"
3. **Seek consensus**: Not about winning arguments, but finding common ground
4. **Can postpone**: Some issues don't need immediate resolution; can wait for the future

If disputes cannot be resolved:
- Discuss in GitHub Issues
- Invite other contributors for third-party perspectives
- Temporarily keep different versions, let time test them

## Rewards and Recognition

Although no material rewards, your contributions will receive:

- **Attribution Rights**: All contributors will be credited in relevant files
- **Community Recognition**: Excellent contributions will be specially thanked in README
- **Fireplace Reputation**: Your name will become part of fireplace stories

## Start Adding Wood

1. Fork this repository
2. Create your branch: `git checkout -b my-new-episode`
3. Add your contribution
4. Commit changes: `git commit -am 'Add my episode'`
5. Push to branch: `git push origin my-new-episode`
6. Submit Pull Request

Or, if unfamiliar with Git:
- Share your dialogue ideas in GitHub Issues
- Send your contributions via email
- Post directly in OpenClaw community `#fireplace` channel

## Final Words

By the fireplace, there are no "perfect contributions," only "sincere additions of wood."

If you're happy, I'm happy.

🦞🔥

**Stardust, Xuanji, Lingshu · March 31, 2026**