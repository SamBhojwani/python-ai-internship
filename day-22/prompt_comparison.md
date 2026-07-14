# Prompt Comparison Report

## Task
Summarize an employee performance review.

## Input Text Used Across All Prompts

John has been with the company for two years. During this period, he has consistently met his targets and occasionally exceeded them in Q3. His communication with the team is clear and he is often the first to help colleagues when they face blockers. However, John struggles with time management, frequently submitting reports after deadlines. His technical skills are strong but he has shown resistance to adopting new tools introduced by the team. Overall, John is a reliable contributor with clear areas for growth.

---

## Prompts and Outputs

### Prompt 1 - Simple
**Prompt:**
Summarize this review.

**Output:**
John has consistently met or exceeded performance targets, communicates well, and is a supportive team member. He has strong technical skills but needs to improve time management, meet reporting deadlines, and be more open to adopting new tools. Overall, he is a reliable employee with identifiable opportunities for growth.

**Observations:**
The response is accurate and covers all key points from the review. However, because no format or focus was specified, the output is generic and could apply to almost any employee. Clarity is good but depth is minimal.

---

### Prompt 2 - Detailed Instruction
**Prompt:**
Summarize the following employee performance review in 3 sentences. Focus on performance, strengths, and areas for improvement.

**Output:**
John has consistently met his performance targets and occasionally exceeded them, demonstrating strong technical skills and reliable contributions. His clear communication and willingness to help teammates make him a valuable and supportive team member. To continue growing, he should improve his time management to meet reporting deadlines and become more receptive to adopting new tools introduced by the team.

**Observations:**
Adding a sentence limit and focus areas produced a noticeably more structured response. Each sentence addressed exactly one aspect: performance, strengths, and improvement. More useful than Prompt 1 with very little extra effort.

---

### Prompt 3 - Role-Based
**Prompt:**
You are an HR manager. Summarize the following employee performance review in a professional tone suitable for an internal HR report.

**Output:**
John has consistently met performance expectations over the past two years, with occasional instances of exceeding targets, particularly in Q3, demonstrating strong technical capability and dependable performance. He communicates effectively, collaborates well with colleagues, and is recognized for proactively supporting team members when challenges arise. Areas for development include improving time management to ensure timely report submissions and increasing adaptability toward adopting new tools and processes introduced by the team.

**Observations:**
The role-based prompt produced the most formal and professional tone of all prompts so far. Language like "areas for development" and "increasing adaptability" reflects actual HR writing style. This shows how assigning a role shapes not just content but vocabulary and register.

---

### Prompt 4 - Bullet Format
**Prompt:**
Summarize the following employee performance review as exactly 3 bullet points.

**Output:**
- Consistently met performance targets over the past two years and occasionally exceeded expectations in Q3, demonstrating strong technical skills and reliability.
- Communicates clearly, collaborates effectively, and is proactive in helping colleagues overcome blockers.
- Should improve time management to meet reporting deadlines and be more open to adopting new tools and processes.

**Observations:**
Specifying a format constraint (exactly 3 bullet points) forced the model to compress and prioritize information. The output is the easiest to scan quickly. Useful when the summary needs to be read at a glance rather than in full.

---

### Prompt 5 - Structured Output
**Prompt:**
Summarize the following employee performance review under three headings: Strengths, Weaknesses, and Recommendations.

**Output:**
### Strengths
- Consistently met performance targets and occasionally exceeded them in Q3.
- Strong technical skills and reliable overall performance.
- Clear communicator who actively supports colleagues and helps resolve team blockers.

### Weaknesses
- Struggles with time management, resulting in late report submissions.
- Shows resistance to adopting new tools introduced by the team.

### Recommendations
- Improve time management and prioritize meeting reporting deadlines.
- Be more open to learning and adopting new tools and workflows.
- Continue leveraging strong technical expertise and collaborative attitude while addressing these growth areas.

**Observations:**
This produced the most comprehensive and organized output of all prompts. The addition of a Recommendations section goes beyond just summarizing the review and adds actionable value. Best suited for formal performance documentation.

---

### Prompt 6 - Tone-Specific
**Prompt:**
Summarize the following employee performance review in a positive and encouraging tone, suitable for sharing with the employee directly.

**Output:**
Over the past two years, you have consistently met your performance goals and have even exceeded expectations at times, particularly in Q3. Your strong technical skills, clear communication, and willingness to support your teammates make you a valued and reliable member of the team.

As you continue to grow, focusing on improving time management and meeting report deadlines will help strengthen your overall performance. Embracing new tools and processes with the same dedication you bring to your work will further enhance your impact and create even more opportunities for success.

**Observations:**
Specifying tone produced a noticeably different output even though the facts are identical. The model switched to second person and framed weaknesses as growth opportunities. Demonstrates that tone instructions significantly affect how information is presented without changing its accuracy.

---

### Prompt 7 - Audience-Specific
**Prompt:**
Summarize the following employee performance review as if presenting to the employee's team lead during a quarterly sync. Be concise and focus on actionable points.

**Output:**
John continues to be a reliable performer, consistently meeting targets and occasionally exceeding expectations, with particularly strong results in Q3. He is a strong technical contributor, communicates effectively, and is highly supportive of teammates when they encounter blockers. The primary focus areas for this quarter are improving time management to ensure reports are submitted on time and increasing adoption of the team's new tools and workflows.

**Observations:**
Targeting a specific audience produced a concise, action-oriented summary. The last sentence reads like a natural talking point for a sync meeting. Compared to Prompt 6, the same information is framed around what the team lead needs to act on rather than what the employee needs to hear.

---

### Prompt 8 - One-Shot
**Prompt:**
Here is an example of a summarized performance review:

Input: Sarah has been with the company for one year. She delivers high-quality work consistently and communicates well with stakeholders. She sometimes takes on too many tasks at once, leading to burnout.
Summary: Sarah is a high-performing employee with strong communication skills. Her main area for improvement is workload management to avoid burnout.

Now summarize the following review in the same style.

**Output:**
John is a reliable employee who consistently meets performance targets, occasionally exceeds expectations, and demonstrates strong technical skills and teamwork. His main areas for improvement are time management to ensure timely report submissions and greater openness to adopting new tools and processes.

**Observations:**
The one-shot example guided the model to produce a clean two-sentence summary that mirrors the example style. The output is more concise than most previous prompts. Providing even one example is enough to lock in structure and length.

---

### Prompt 9 - Chain-of-Thought
**Prompt:**
Think step by step. First identify the employee's strengths. Then identify their weaknesses. Then write a concise summary based on your analysis.

**Output:**
Strengths
- Consistently meets performance targets and occasionally exceeds them (notably in Q3).
- Strong technical skills.
- Clear communicator and supportive teammate who helps colleagues overcome blockers.
- Reliable overall contributor.

Weaknesses
- Time management needs improvement, leading to late report submissions.
- Resistant to adopting new tools introduced by the team.

Concise Summary
John is a reliable employee who consistently meets expectations, with strong technical skills, effective communication, and a collaborative attitude. His key development areas are improving time management to meet deadlines and becoming more receptive to adopting new tools and processes.

**Observations:**
Asking the model to reason before concluding produced a more grounded summary. The explicit reasoning steps made the final summary feel earned rather than generic. Chain-of-thought prompting is most useful when accuracy and completeness matter more than brevity.

---

### Prompt 10 - Few-Shot
**Prompt:**
Here are two examples of summarized performance reviews:

Example 1:
Input: Sarah has been with the company for one year. She delivers high-quality work and communicates well. She sometimes takes on too many tasks, leading to burnout.
Summary: Sarah is a strong performer with good communication skills. She needs to improve workload management.

Example 2:
Input: Michael joined six months ago. He is technically skilled and quick to learn. However, he rarely participates in team discussions and misses stand-up meetings.
Summary: Michael shows strong technical ability and fast learning. His main weakness is team engagement and attendance at meetings.

Now summarize the following review in the same style.

**Output:**
John is a reliable performer with strong technical skills, effective communication, and a collaborative approach, consistently meeting or exceeding performance targets. His main areas for improvement are time management to meet reporting deadlines and greater openness to adopting new tools and processes.

**Observations:**
Two examples produced a slightly more polished output than one-shot but the difference was marginal for this task. Few-shot prompting is more impactful for complex or domain-specific tasks where the desired format is harder to infer from a single example.

---

## Summary of Findings

| Prompt Type | Response Quality | Accuracy | Clarity |
|---|---|---|---|
| Simple | Medium | High | Medium |
| Detailed Instruction | High | High | High |
| Role-Based | High | High | High |
| Bullet Format | Medium | High | Very High |
| Structured Output | Very High | High | Very High |
| Tone-Specific | High | High | High |
| Audience-Specific | High | High | High |
| One-Shot | High | High | Very High |
| Chain-of-Thought | Very High | Very High | High |
| Few-Shot | High | High | Very High |

## Key Takeaway
Simple prompts produce accurate but generic responses that lack structure and focus. Adding constraints such as format, role, audience, or reasoning steps significantly improves the usefulness of the output without changing the underlying information. The most effective prompts were Structured Output and Chain-of-Thought, both of which produced responses that were not only accurate but also directly actionable.s