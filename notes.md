Data Engineering Questions asked to ascertain functional and non-functional requirements

1. Business and Goals first - The purpose of every corporate data engineering project is to create business value.
- What decision will this data help you make?
- What does success look like in 90 days?
- What's the cost of NOT having this solution in place at this moment? 

2. Data source questions - Data Engineering is all moving data from source to destination.
- Where does your data live right now?
- Is the app and website data in the same schema or separate?
- How are orders created, is there an API, direct DB writes or message queues?
- How much data are we talking about, rows per day, total table size?
- Is the data ever updated after creation - determines whether we do an incremental load, a full load or a change data capture (CDC)
- Do you have any existing data documentation or schema diagrams?

3. Non-functional requirements
- How fresh does the data need to be? Should it be real-time, hourly, daily, etc.
- How many months of historical data do we need to backfill?
- What happens if the pipeline fails at 3am, does someone need to be woken up?
- What is the acceptable downtime, can the dashboard be down for maintenance?
- Do you have SLAs with customers or stakeholders tied to this data?

4. Stakeholders and access control
- Who are all the consumers of this data?
- Does each person need different views or different levels of access?
- Will this data ever be shared externally, to investors, partners, auditors, etc?
- Who owns the data, who do I go to when requirements change?

5. Technical environment
- Who is the primary user of this dashboard, technical or non-technical?
- What are the three most important numbers you want to see first?
- Will you want the dashboard to be pushed to you via email or will you log in?

6. Reliability and failure
- Have you had data incidents before, what happened and what was the impact?
- How did you find out about the black friday issue, customer complaint or internal
- What is your current monitoring setup?