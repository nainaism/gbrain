# Brain Resolver

This is the top-level decision tree for filing knowledge. Every new page MUST pass through this resolver before creation. Read this before creating any new page.

## Decision Tree

1. **Is it about a person?** → `people/`
2. **Is it about a company or organization?** → `companies/`
3. **Is it about a project (with goals, tasks, deadlines)?** → `projects/`
4. **Is it about a technical concept, framework, or pattern?** → `concepts/`
5. **Is it an original idea, proposal, or insight?** → `ideas/`
6. **Is it about kaede's personal operations or reflections?** → `personal/`
7. **Cannot classify?** → `inbox/` (review weekly, move to proper location)

## Classification Rules

### people/
- Real people: team members, clients, contacts, industry figures
- Include: role, contact info, relationship, key facts
- Slug format: `people/first-last.md` (e.g., `people/narita.md`)

### companies/
- Organizations, companies, open-source projects as entities
- Include: what they do, relationship to us, key facts
- Slug format: `companies/slug.md` (e.g., `companies/nainaism.md`)

### projects/
- Active or completed projects with goals and tasks
- Include: goal, status, members, links to Notion
- Slug format: `projects/slug.md`

### concepts/
- Technical concepts, frameworks, patterns, methodologies
- Include: definition, why it matters, how we use it
- Slug format: `concepts/slug.md`

### ideas/
- Original thinking, proposals, insights from 成田さん
- Include: the idea itself, context, status
- Slug format: `ideas/slug.md`

### inbox/
- Unclassified items awaiting review
- Review weekly, move to proper location

### personal/
- Kaede's operational notes, reflections, learnings
- Not for facts about other people or entities
