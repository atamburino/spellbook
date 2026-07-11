# Relationship Between AI, Machine Learning, and Deep Learning

## Learning goal

Explain how artificial intelligence, machine learning, neural networks, and deep learning relate - and when deep learning is or is not a sensible choice.

## The relationship in one picture

```text
Artificial intelligence (largest field)
└── Machine learning (AI systems that learn patterns from data)
    └── Neural networks (one family of ML models)
        └── Deep learning (complex neural networks with many layers/parameters)
```

**The sentence to remember:** Deep learning is a type of machine learning, and machine learning is one part of artificial intelligence. The reverse is not true. Not all AI uses machine learning, and not all machine learning uses deep learning. [Course source: Chapter 1, pp. 1-2 and 74-76](../sources/chapter-1.pdf#page=2)

## Start with the four terms

### Artificial intelligence (AI)

AI is the broad field of building algorithms and models that perform tasks associated with human thought, such as recognizing patterns, making predictions, generating outputs, or reasoning. The textbook identifies six AI domains: machine learning, computer vision, natural language processing, knowledge representation, automated reasoning, and robotics. [Course source: Chapter 1, pp. 72-75](../sources/chapter-1.pdf#page=73)

### Machine learning (ML)

Machine learning is a subset of AI. Instead of receiving an explicit rule for every situation, an ML model learns statistical patterns from data and uses those patterns to make predictions or decisions. [Course source: Chapter 1, p. 2](../sources/chapter-1.pdf#page=2)

### Neural network

A neural network is one family of machine-learning models. It connects layers of artificial neurons. Training changes numerical **weights** so that inputs produce more useful outputs. A perceptron is a simple neural-network model; a multilayer perceptron adds hidden layers. [Course source: Chapter 1, pp. 10-18 and 48-50](../sources/chapter-1.pdf#page=10)

### Deep learning (DL)

Deep learning is the part of machine learning that uses complex neural networks with multiple layers and many learned parameters. The word **deep** refers to depth in the network's layers, not to humanlike depth of thought. These layers allow a model to learn complicated relationships, but those relationships can be difficult to interpret. [Course source: Chapter 1, pp. 2 and 76-78](../sources/chapter-1.pdf#page=76)

## WoW analogy: the professions menu

Imagine all possible ways to build a useful WoW character:

- **AI is the entire character system.** It includes every way a character can behave intelligently.
- **Machine learning is the professions menu.** It is one important section of the larger system.
- **Neural networks are one profession**, such as blacksmithing.
- **Deep learning is a highly developed blacksmithing specialization** with many connected recipes and dependencies.

Every deep-learning build is inside the machine-learning menu, but the menu contains other professions too. Likewise, every machine-learning system belongs to AI, but AI also includes approaches outside machine learning. [Relationship supported by Chapter 1, pp. 1-2 and 74-76](../sources/chapter-1.pdf#page=1)

### Where the analogy breaks

The categories are not optional game-menu choices with fixed boundaries. Neural-network depth, size, and complexity exist on a spectrum. Also, modern applications can combine several AI domains and several models, while a game profession is a much cleaner category. [Course source for deep-learning complexity: Chapter 1, pp. 76-78](../sources/chapter-1.pdf#page=76)

## Traditional ML versus deep learning

Here, **traditional ML** means non-deep model families such as linear models, decision trees, nearest-neighbor methods, and support vector machines. It does not mean outdated or inferior.

| Question | Traditional ML | Deep learning |
| --- | --- | --- |
| What models are typical? | Linear models, trees, ensembles, SVMs | Multilayer neural networks |
| What data fits naturally? | Often structured rows and columns | Often text, images, audio, and other complex inputs |
| Who identifies useful features? | A person often selects or engineers more features | The network can learn useful internal representations through its layers |
| How much data and compute? | Often works with less | Complex networks commonly require more |
| Can people explain it? | Simpler models are often easier to inspect | Learned relationships are often difficult to interpret |
| Is it always less accurate? | No | No - performance depends on the task and evidence |

The textbook directly supports the differences in layers, parameter count, complexity, learned features, compute history, and interpretability. The final row is a model-selection principle: neither approach is universally best. [Course source: Chapter 1, pp. 2, 36, and 76-78](../sources/chapter-1.pdf#page=2)

## What is a feature?

A **feature** is an input value the model can use.

For a house-price model, features could include:

- number of bedrooms;
- square footage;
- location; and
- age of the house.

The desired output - the house price - is the **target**. The textbook's multilayer-perceptron example uses bedrooms and square footage as inputs and predicted list price as its output. [Course source: Chapter 1, pp. 48-49](../sources/chapter-1.pdf#page=48)

### Feature engineering

**Feature engineering** means choosing or transforming raw information into useful model inputs.

Example: A traditional model may receive a manually created `distance_to_auction_house` value. A deep image model may instead learn increasingly useful internal patterns from pixels across multiple layers. The textbook describes deep learning as automatically extracting features and gives an image progression from edges to shapes to complex objects. [Course source: Chapter 1, p. 2](../sources/chapter-1.pdf#page=2)

Deep learning reduces some manual feature engineering; it does not remove human work. People still choose data, targets, architecture, evaluation methods, and deployment rules. The textbook's bike-share case study demonstrates the continuing need to explore feature coding and remove confounded inputs before training a neural network. [Course source: Chapter 1, pp. 59-65](../sources/chapter-1.pdf#page=59)

## How learning happens in a neural network

1. **Forward propagation:** Input moves through the network to produce a prediction.
2. **Loss calculation:** A loss function measures the difference between the prediction and expected result.
3. **Backpropagation:** The training process calculates how weights contributed to the error.
4. **Weight update:** The weights are adjusted to reduce future error.
5. **Repeat:** The network trains over more examples and epochs.

This is learning in the mathematical sense: repeated parameter adjustment. It is not consciousness or human understanding. [Course source: Chapter 1, pp. 48-54](../sources/chapter-1.pdf#page=48)

## Example: predicting WoW auction-house prices

### Traditional ML approach

Build a table with features such as item type, realm population, recent median price, day of week, and available quantity. Train a regression model to predict the next price.

Why it may fit:

- The inputs are already structured.
- A smaller dataset may be useful.
- A person may need to explain which inputs influenced the prediction.

These advantages follow from the textbook's contrast between simpler relationships and deep models' complexity and interpretability limits. [Course source: Chapter 1, pp. 76-78](../sources/chapter-1.pdf#page=76)

### Deep-learning approach

Give a neural network a much larger stream of auction history, item descriptions, market sequences, and perhaps screenshots. The network learns complex interactions across these inputs.

Why it may fit:

- There is abundant data.
- The inputs include complex text, images, or time-dependent patterns.
- Predictive performance matters more than having a simple explanation.

The textbook identifies deep learning as useful for complicated relationships and image or speech recognition, and it discusses nonlinear and seasonal data in its neural-network examples. [Course source: Chapter 1, pp. 2, 36-46, and 59-60](../sources/chapter-1.pdf#page=2)

### The lesson

Using deep learning merely because it sounds more advanced could waste compute and make the result harder to explain. Model choice should follow the problem, data, constraints, and evaluation results. [Course source for complexity and interpretability tradeoffs: Chapter 1, pp. 76-78](../sources/chapter-1.pdf#page=76)

## When a simpler ML model may be better

Prefer testing a simpler model when:

- the data is a modest structured table;
- decisions must be explainable;
- training or prediction must be inexpensive;
- little training data is available; or
- the simple model already meets the measured requirement.

This is a practical inference from the textbook's description of deep learning as complex, parameter-heavy, compute-dependent, and difficult to interpret. [Course source: Chapter 1, pp. 76-78](../sources/chapter-1.pdf#page=76)

## When deep learning may be better

Consider deep learning when:

- the data contains images, audio, text, or complicated nonlinear patterns;
- enough useful data and compute are available;
- learning representations automatically is valuable; and
- evaluation shows a meaningful improvement over simpler baselines.

The first three conditions follow from the textbook's descriptions and examples. The last is the verification step that prevents choosing a model only because of its label. [Course source: Chapter 1, pp. 2, 36-46, 51-54, and 76-78](../sources/chapter-1.pdf#page=2)

## Common mistakes to avoid

- **"AI and ML are synonyms."** ML is only one AI domain. [Chapter 1, pp. 74-75](../sources/chapter-1.pdf#page=74)
- **"All ML is deep learning."** Deep learning is one part of ML. [Chapter 1, pp. 1-2 and 76](../sources/chapter-1.pdf#page=2)
- **"All neural networks are deep."** A single-layer perceptron is a neural network, while the chapter separately introduces multilayer networks and deep learning. [Chapter 1, pp. 18-36 and 48-50](../sources/chapter-1.pdf#page=18)
- **"Deep learning understands like a person."** Training adjusts weights to reduce measured error. [Chapter 1, pp. 48-54](../sources/chapter-1.pdf#page=48)
- **"Deep learning is always best."** Greater complexity introduces compute and interpretability tradeoffs; models must be evaluated for the actual task. [Chapter 1, pp. 51-54 and 76-78](../sources/chapter-1.pdf#page=51)

## A 20-second decision test

Ask:

1. Is this even an ML problem, or could explicit rules solve it?
2. Is my data mostly a structured table or complex raw content?
3. Do I have enough examples and compute?
4. Must I explain individual predictions?
5. Did deep learning actually beat a simpler baseline on the metric that matters?

## From-memory explanation

Complete this without looking above:

> AI is the broad field of ___. Machine learning is the part that ___. Neural networks are ___. Deep learning uses ___. Therefore, every deep-learning model is ___, but not every machine-learning model is ___.

## Retrieval check

1. Is all machine learning deep learning? Why not?
2. Can an AI application exist without machine learning?
3. What makes a neural network "deep"?
4. What is feature engineering, and why does deep learning change it?
5. Give one reason to choose traditional ML and one reason to choose deep learning.
6. Where does the WoW analogy stop matching reality?

## Sources and verification

### Course source

- zyBooks, *CS-530 Chapter 1*. Local source: [chapter-1.pdf](../sources/chapter-1.pdf). Primary pages used: 1-2, 10-18, 36-60, and 72-80.

### External sources

- None used for this note. All factual claims and examples derived from claims are tied to the local course chapter above.

## Verification notes

- Verified against the local PDF on **July 11, 2026**.
- The repo currently contains the PDF but no Chapter 1 Markdown conversion. If a conversion is added later, link it here and retain PDF page numbers so the original source remains easy to audit.
