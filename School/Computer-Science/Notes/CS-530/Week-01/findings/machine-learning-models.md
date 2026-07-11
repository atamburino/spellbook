# Differentiating Machine-Learning Models

## Learning goal

Explain what a machine-learning model is, recognize the major kinds of models, and avoid confusing a model's mathematical family with a commercial model name.

## The most important distinction

The word **model** is used at several levels. This causes much of the confusion.

1. A **model family** is a general mathematical approach, such as linear regression, a decision tree, or a neural network.
2. A **trained model** is one particular result of training a model family on data.
3. A **foundation model** is a large, broadly trained model that can be adapted to many tasks.
4. A **product model name** identifies a released model, such as Claude Sonnet 5, GPT-5.6 Sol, or Gemma 4.
5. An **AI system** is the larger application around one or more models. It may also contain prompts, tools, databases, safety classifiers, and ordinary code.

Claude Sonnet 5 and GPT-5.6 Sol are different released models, but both belong to the much broader neural-network and large-language-model categories. Comparing them does not teach us all the major families of machine-learning models.

### WoW analogy

- **Model family:** A character class, such as warrior, mage, or priest.
- **Training algorithm:** The process used to level and build the character.
- **Training data:** The quests, fights, and experiences the character learns from.
- **Trained model:** One particular level-80 character with its learned build and stats.
- **Model release name:** That character's name and version on the roster.
- **AI system:** The complete raid group, including the characters, strategy, add-ons, voice chat, and raid leader.

### Where the analogy breaks

A trained model does not remember its training examples as a game character remembers a completed quest log. Training adjusts numerical parameters so the model captures patterns. Also, a product can silently route work among multiple models, while a WoW character is normally one visible character.

## Algorithm versus model

An **algorithm** is a procedure: a set of steps for doing something. A **training algorithm** examines data and adjusts values called **parameters**. The resulting learned function is the **trained model**.

Think of a cooking recipe as the algorithm and the finished meal as the model. The ingredients and cooking conditions affect the result, even when the recipe is the same.

## Three questions that organize the field

When someone names a model, ask three separate questions:

1. **How does it learn?** Supervised, unsupervised, semi-supervised, self-supervised, or reinforcement learning?
2. **What task does it perform?** Classification, regression, clustering, generation, ranking, anomaly detection, or another task?
3. **What model family or architecture does it use?** Linear model, tree, nearest neighbors, support vector machine, neural network, transformer, and so on?

These labels overlap. For example, a neural network can be trained with supervised learning to perform classification. It is not meaningful to ask whether it is "a neural network or a classification model" because those labels answer different questions.

## How models learn

### Supervised learning

The training examples include both inputs and known correct outputs, called **labels**.

Example: Past email messages are labeled `spam` or `not spam`. The model learns to label a new email.

### Unsupervised learning

The training data has no provided correct answers. The model looks for structure or patterns.

Example: Group players by similar play behavior without supplying names for the groups beforehand.

### Semi-supervised learning

Training uses a small amount of labeled data and a larger amount of unlabeled data. This is useful when labels are expensive to produce.

### Self-supervised learning

The data supplies its own learning target. A language model can hide or predict parts of text and learn from whether its prediction matched the original text. Modern foundation models commonly use self-supervised pretraining.

### Reinforcement learning

An **agent** takes actions in an environment and receives rewards or penalties. It learns a strategy, called a **policy**, that attempts to earn more reward over time.

Example: A game-playing agent receives a positive reward for winning and learns which actions tend to lead to wins.

## What models do

| Task | Output | Beginner example |
| --- | --- | --- |
| Classification | A category | Spam or not spam |
| Regression | A number | Predicted house price |
| Clustering | Groups discovered in data | Similar customer groups |
| Generation | New content | Text, images, audio, or code |
| Ranking/recommendation | An ordered selection | Items a player may want next |
| Anomaly detection | An unusual-case score or label | Suspicious account activity |

**Classification** and **regression** describe tasks, not single algorithms. A decision tree and a neural network can each be used for both tasks.

## Major model families

### Linear and logistic models

A linear model combines input features using learned weights. Linear regression predicts numbers. Logistic regression, despite its name, is commonly used for classification.

- **Strengths:** Fast, needs relatively little compute, and is often interpretable.
- **Weaknesses:** A simple linear form may miss complicated relationships.
- **Good first choice:** Structured table data with a relationship that is approximately simple.

### Decision trees

A tree learns a chain of decision rules, similar to a flowchart.

- **Strengths:** Easy to visualize and explain; handles nonlinear rules.
- **Weaknesses:** A single deep tree can memorize training data and change substantially after small data changes.
- **Typical tasks:** Classification and regression.

### Ensembles

An ensemble combines many models. Random forests combine many decision trees; gradient-boosted trees build trees that successively correct earlier errors.

- **Strengths:** Often excellent on structured, tabular data.
- **Weaknesses:** Harder to explain than one small tree and usually more computationally expensive.
- **WoW analogy:** One raid member's mistake may wipe the group; a coordinated raid uses the judgments of many members. The analogy breaks because ensemble outputs are combined mathematically, not through conversation.

### Nearest-neighbor models

A nearest-neighbor model predicts using the most similar stored examples.

- **Strengths:** Intuitive and involves little conventional training.
- **Weaknesses:** Prediction can become slow with large datasets, and "similar" depends heavily on feature scaling and distance choice.

### Support vector machines

A support vector machine tries to place a boundary between classes with as much separation, or **margin**, as possible. Kernel methods can represent nonlinear boundaries.

- **Strengths:** Can work well on medium-sized datasets with many features.
- **Weaknesses:** Can be slow on very large datasets and less intuitive to explain.

### Probabilistic models

Models such as Naive Bayes make predictions using probabilities and assumptions about how the data was produced.

- **Strengths:** Often fast and effective for tasks such as text classification.
- **Weaknesses:** Simplifying assumptions may not match reality.

### Clustering models

Algorithms such as k-means group examples based on similarity without being given group labels.

- **Strengths:** Helps explore unlabeled data.
- **Weaknesses:** A discovered cluster is not automatically a meaningful real-world category. The number of groups and the definition of similarity matter.

### Neural networks

A neural network contains connected layers of artificial neurons. Training adjusts many weights so the network maps inputs to outputs.

- **Strengths:** Learns complex patterns and works especially well with text, images, audio, and other unstructured data.
- **Weaknesses:** Often needs more data and compute and is usually harder to interpret.

A **deep-learning model** is a neural network with multiple learned layers or, more broadly, substantial depth and many parameters. Chapter 1 introduces the perceptron and multilayer perceptron as early neural-network forms (chapter PDF, pp. 18-59) and describes deep learning as complex models that capture difficult relationships but are hard to interpret (pp. 76-78).

### Transformers and large language models

A transformer is a neural-network architecture that uses attention mechanisms to relate parts of its input. A **large language model (LLM)** is a large model trained to process and generate language; most current LLMs use transformer-based architectures.

Claude, GPT, and Gemma are examples in this area. They are not alternatives to the entire list above: they are members of one advanced branch of it.

## Named model labels describe different axes

### Frontier model

**Frontier model** is an industry and policy label for a developer's most capable, general-purpose models near the current edge of capability. It is not a distinct mathematical architecture. The boundary changes as newer models appear.

As of July 11, 2026:

- Anthropic describes Claude Opus 4.8 as a generally more capable model and Sonnet 5 as a lower-cost model that approaches Opus performance on some agentic tasks.
- OpenAI lists GPT-5.6 Sol as its frontier model for complex professional work, with Terra and Luna offering different intelligence/cost tradeoffs.

These product tiers mainly communicate capability, cost, speed, and intended workload. They do not tell us the complete architecture or training recipe.

### Foundation model

A foundation model is trained broadly enough to support many downstream tasks. It may later be prompted, fine-tuned, connected to tools, or incorporated into a specialized application.

**Foundation** describes breadth and adaptability. **Frontier** describes being near the current capability boundary. A model can be both, either, or neither.

### General-purpose versus specialized model

- A **general-purpose model** handles many kinds of tasks.
- A **specialized model** is designed or adapted for a narrower task, such as embeddings, moderation, speech recognition, medical images, or cybersecurity classification.

A specialized model may outperform a larger general model on its target task while being smaller, cheaper, and easier to evaluate.

### Proprietary, open-weight, and open-source

These terms describe **access and licensing**, not intelligence.

- **Proprietary/closed model:** The provider keeps the learned weights and much of the training process private. Users normally access the model through an application or API.
- **Open-weight model:** The learned numerical parameters are downloadable under specified license terms. A user may run and often fine-tune the model on controlled hardware.
- **Open-source AI:** Under the Open Source Initiative's definition, meaningful access also includes the necessary code, parameter access, and sufficiently detailed training-data information under appropriate terms.

Your rough understanding was close: open-weight models can often be run locally, but the released weights do not necessarily include the original training data or complete training process. Therefore, **open weight** is safer and more precise than automatically calling every downloadable model **open source**.

Google describes Gemma 4 as an **open model** whose weights can run on local hardware or hosted services. OpenAI similarly publishes the open-weight `gpt-oss` models. Local use still requires enough memory and compute, and the license still matters.

## Fable 5: model versus safety system

The name you remembered as "Fayable 5" is **Claude Fable 5**.

Anthropic says Fable 5 and Mythos 5 share the same underlying model. Fable adds stronger safeguards for general access. On certain flagged topics, a request may receive an answer from Opus 4.8 instead. Anthropic also describes a safety classifier that can block requests.

The key architecture lesson is that an AI product may be a **system of models**:

```text
User request
    |
    v
Safety classifier / routing rules
    | safe                         | flagged
    v                              v
Fable 5                       refusal or Opus 4.8
    |                              |
    +--------------+---------------+
                   v
               response
```

It is reasonable to summarize this as "one model checks or routes work for another" at a high level. More precisely, the public description refers to safeguards, routing, and a classifier; it does not establish that Fable simply has a second general chat model debate every answer.

## A practical model-comparison checklist

Do not ask only, "Which model is best?" Ask:

1. What output do I need: category, number, group, ranking, or generated content?
2. What kind and amount of data do I have?
3. Is the data structured in rows and columns, or unstructured text, images, and audio?
4. How costly is a wrong answer?
5. Must a person be able to explain the prediction?
6. What limits exist for latency, money, memory, and compute?
7. Must the data remain on local or controlled infrastructure?
8. Do I need to modify or fine-tune the model?
9. What evidence shows the model works on this particular task?

A larger or newer model is not automatically the correct model. For example, interpretable logistic regression may be preferable to a frontier LLM for a small, structured, high-stakes classification problem.

## From-memory explanation

Fill this in without looking back:

> A machine-learning model is...
>
> Classification differs from a model family because...
>
> Claude, GPT, and Gemma represent only one part of machine learning because...
>
> Open weight does not always mean open source because...

## Retrieval check

1. What is the difference between an algorithm and a trained model?
2. Why can a decision tree be both a classification model and a regression model?
3. Is every neural network a frontier model? Is every frontier model necessarily open weight?
4. Which learning approach begins with examples that already have correct labels?
5. Why could a smaller model be better than a frontier LLM?
6. Is Fable 5's safety routing part of the underlying model, the surrounding system, or potentially both?

## Sources

### Course source

- zyBooks, *CS-530 Chapter 1*, pp. 1-6 (AI, ML, deep learning, generative and discriminative models, and language models); pp. 18-59 (perceptrons and multilayer perceptrons); pp. 72-80 (AI domains, deep learning, and responsible AI use). Local copy: [chapter-1.pdf](../sources/chapter-1.pdf).

### External verification

- [Anthropic: Introducing Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5) - Sonnet 5, Opus 4.8 comparison, and safety routing.
- [Anthropic: Claude Fable 5 and Claude Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5) - shared underlying model and Fable safeguards.
- [Anthropic: Redeploying Fable 5](https://www.anthropic.com/news/redeploying-fable-5) - safety classifier and fallback routing to Opus 4.8.
- [OpenAI API: All models](https://developers.openai.com/api/docs/models/all) - current GPT-5.6 product tiers and model categories.
- [OpenAI: Open models](https://openai.com/open-models/) - `gpt-oss` open-weight models and licensing.
- [Google AI for Developers: Gemma models overview](https://ai.google.dev/gemma/docs) - Gemma 4 capabilities, weights, local use, and customization.
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide) - established supervised and unsupervised model families.
- [Open Source Initiative: Open Source AI Definition 1.0](https://opensource.org/ai/open-source-ai-definition) - distinction between model weights and open-source AI requirements.

## Verification notes

- Checked on **July 11, 2026**. Named frontier products and provider recommendations change quickly; recheck official model pages before using them in the final journal.
- The course PDF's statement that GPT-4 had an estimated 1.7 trillion parameters (p. 78) should not be repeated as established fact without stronger evidence. OpenAI has not publicly documented GPT-4's parameter count in the sources used here.
