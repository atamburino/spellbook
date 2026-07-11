---
assignment: Module One Activity
date: July 11, 2026
author: Andy Tamburino
course: CS 530
title: Machine Learning and Deep Learning
subtitle: Evaluating GitHub Copilot as a Research Tool
---

## The Relationship Between Machine Learning and Deep Learning

When I considered how I was using the term model before this assignment, I had limited my use of that term primarily to major generative artificial intelligence (AI) products such as Gemini, Claude, and ChatGPT. My conversation with GitHub Copilot and the readings associated with this assignment expanded my previous definition. They helped me view a model not just as a specific AI-based product, but as the chosen methodology for solving a particular problem. That shift has provided me with a greater overall understanding of both machine learning and deep learning methodologies, as well as a better way to assess Copilot as a research tool.

Machine learning is a large category of AI in which systems are trained to recognize patterns in data to generate predictions, classifications, or decisions. Deep learning is a subset of machine learning that uses neural networks with multiple layers (zyBooks, 2026, Section 1.1).

While all deep learning models are machine learning models, not all machine learning models are deep learning models. The difference between these two areas of AI is significant because of their differing design goals. As noted in the course text, traditional models, such as regression and decision trees, work effectively for problems in which data is structured and features are known. In addition, they typically require less data and computing power than deep learning models. The results produced by traditional models are also generally easier to understand and interpret.

Deep learning models are capable of automatically learning complex representations of data. They are particularly useful for applications involving language, images, and audio. However, they typically require much larger amounts of data and significantly more computing resources than traditional models. Additionally, the results of deep learning models can be difficult to understand and interpret.

As a direct result of my new understanding of machine learning versus deep learning, I now think differently about the questions I need to ask when designing a model. Rather than first asking which major language model I should use for a project, I will now ask: What problem am I solving? What data am I using? Do the results need to be explainable? Finally, what complexity am I willing to tolerate?

A simple classification problem may not necessarily require a deep learning network. On the other hand, problems that involve generating text or analyzing unstructured data may require more sophisticated modeling techniques. Generative AI does not replace the entire scope of machine learning methodologies. It simply represents one highly visible application of those methods.

My new understanding also relates directly to my professional work. Recently, I used an AI assistant to automate the creation of AWS infrastructure using the Cloud Development Kit (CDK) and TypeScript. Once I created and tested a reusable construct, the AI assistant repeated that pattern in other places throughout my codebase. While it accelerated repetitive implementation tasks, I remained ultimately responsible for ensuring the validity and soundness of the architecture being implemented.

Ultimately, this experience reinforced my opinion that the best model for a given task is not automatically the newest. It is the model and workflow that most effectively solve the problem at hand while accounting for its associated risks.

## GitHub Copilot's Effectiveness

A large part of my opinion about GitHub Copilot stems from almost one and a half years of professional use. I think it is effective, particularly inside Visual Studio Code, which brings the conversation closer to the code and provides tools and context to the model. During this activity, Copilot organized ideas, compared methods, and offered a place to start further questioning. Most importantly, however, it helped me see how narrowly I had been thinking about models.

Evaluating Copilot solely on its language model would be inaccurate. Copilot is a tool designed to manage prompts, instructions, context, and other tools used to create a response. When the harness managing these interactions limits how a user can work with the model, even a well-designed model may appear to have limitations.

Earlier versions of Copilot also used file structures that differed from those used by tools such as Claude Code, requiring overlapping instruction files. Copilot later began using some common file structures; however, this experience made me realize that what appears to be a limitation of a model could actually be caused by the tool or product surrounding it.

Although Copilot provided good explanations for many of my questions, confidence does not necessarily equate to accuracy. It was most helpful when I posed additional questions, requested comparative analysis, and tied the information back to something I understood. Copilot's answers still needed to be verified, consistent with zyBooks' advice that AI-generated output should be reviewed for errors (zyBooks, 2026, Section 1.8).

Prompt quality also affected Copilot's usefulness. Broadly worded questions yielded broad answers. However, questions that requested comparisons using specific criteria resulted in higher-quality responses.

Based on my experience, I do not believe Copilot is the best harness for every workflow. While it has strengths related to integration and flexibility, providing a single interface across models from multiple developers creates tradeoffs regarding feature sets, limits, and costs. Therefore, I view it as a solid option rather than an all-in-one solution.

## Conclusion

This assignment helped me realize that model families exist for many reasons, including the type of data being used and the problem being solved. It also helped me understand that evaluating an AI assistant requires evaluating the entire system. Copilot's limitations were interesting because they forced me to think about validation and even the construction of my own prompts. I am now focusing much less on the new models released each month. Instead, I have shifted my focus toward why a particular architecture makes sense for a given problem and how it can be used responsibly. To me, that is one of the best parts of being a software developer.

## References

zyBooks. (2026). CS 530: AI principles and applications (Ch. 1: Machine learning and deep learning). zyBooks, a Wiley brand. [https://learn.zybooks.com/zybook/CS-530-10101.202657-1](https://learn.zybooks.com/zybook/CS-530-10101.202657-1)
