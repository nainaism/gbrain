     1|# Brain Resolver
     2|
     3|This is the top-level decision tree for filing knowledge. Every new page MUST pass through this resolver before creation. Read this before creating any new page.
     4|
     5|## Decision Tree
     6|
     7|1. **Is it about a person?** → `people/`
     8|2. **Is it about a company or organization?** → `companies/`
     9|3. **Is it about a project (with goals, tasks, deadlines)?** → `projects/`
    10|4. **Is it about a technical concept, framework, or pattern?** → `concepts/`
    11|5. **Is it an original idea, proposal, or insight?** → `ideas/`
    12|6. **Is it about kaede's personal operations or reflections?** → `personal/`
    13|7. **Cannot classify?** → `inbox/` (review weekly, move to proper location)
    14|
    15|## Classification Rules
    16|
    17|### people/
    18|- Real people: team members, clients, contacts, industry figures
    19|- Include: role, contact info, relationship, key facts
    20|- Slug format: `people/first-last.md` (e.g., `people/narita.md`)
    21|
    22|### companies/
    23|- Organizations, companies, open-source projects as entities
    24|- Include: what they do, relationship to us, key facts
    25|- Slug format: `companies/slug.md` (e.g., `companies/nainaism.md`)
    26|
    27|### projects/
    28|- Active or completed projects with goals and tasks
    29|- Include: goal, status, members, links to Notion
    30|- Slug format: `projects/slug.md`
    31|
    32|### concepts/
    33|- Technical concepts, frameworks, patterns, methodologies
    34|- Include: definition, why it matters, how we use it
    35|- Slug format: `concepts/slug.md`
    36|
    37|### ideas/
    38|- Original thinking, proposals, insights from 成田さん
    39|- Include: the idea itself, context, status
    40|- Slug format: `ideas/slug.md`
    41|
    42|### inbox/
    43|- Unclassified items awaiting review
    44|- Review weekly, move to proper location
    45|
    46|### personal/
    47|- Kaede's operational notes, reflections, learnings
    48|- Not for facts about other people or entities
    49|

## See Also
- [[concepts/hermes-agent]]
- [[concepts/gbrain]]
- [[concepts/ai-factory]]
