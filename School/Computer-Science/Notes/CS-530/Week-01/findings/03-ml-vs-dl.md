# Traditional Machine Learning vs. Deep Learning

## Main distinction
Traditional machine learning usually depends more on human-designed features and smaller, more structured datasets. Deep learning can learn features automatically from raw data and often performs better on unstructured data.

## Key differences
- Feature engineering: more manual in traditional ML, more automatic in deep learning.
- Data needs: traditional ML often needs less data; deep learning usually needs much more.
- Computation: deep learning is more expensive.
- Interpretability: traditional ML is often easier to explain.

## Neural networks as the bridge between machine learning and deep learning
Neural networks connect machine learning and deep learning because they are the core structure used by many deep learning systems. A neural network is a model that learns patterns by passing information through layers of connected units.

### Neurons
- Plain-language definition: A neuron is a small processing unit that receives information, combines it, and sends an output onward.
- WoW analogy: A neuron is like a raid member who receives signals from teammates, weighs what matters, and decides how to respond.

### Layers
- Plain-language definition: Layers are groups of neurons arranged in steps. Early layers detect simple features, while later layers combine them into more complex patterns.
- WoW analogy: The first layer is like a tank or healer noticing obvious combat cues, while later layers are like the raid leader combining movement, cooldowns, and positioning into a full strategy.

### Weights
- Plain-language definition: Weights are numbers that tell the network how much importance to give each input.
- WoW analogy: A weight is like how strongly a player values a particular warning signal, such as a boss cast bar or a healer’s callout.

### Activation functions
- Plain-language definition: Activation functions decide whether a neuron should pass along its signal or stay mostly inactive.
- WoW analogy: This is like a player deciding whether a cue is important enough to act on right away, such as whether to interrupt a spell or move out of a fire.

### Training
- Plain-language definition: Training is the process of showing the network many examples and adjusting its internal parameters so it makes better predictions.
- WoW analogy: Training is like practicing raid encounters over and over until the team gets better at reacting to mechanics.

### Loss functions
- Plain-language definition: A loss function measures how wrong the model’s prediction is compared with the correct answer.
- WoW analogy: A loss function is like a raid leader judging how badly the team performed on a pull, based on mistakes, timing, and damage taken.

### Backpropagation
- Plain-language definition: Backpropagation is the method used to update the model by sending error information backward through the network so it can adjust its weights.
- WoW analogy: It is like the raid leader reviewing the encounter afterward, identifying what went wrong, and giving instructions for the next attempt.

## Deep learning vs. traditional machine learning

### 1. Feature engineering
- Traditional machine learning often requires humans to decide which features matter most. For example, a model predicting loan risk might use income, debt, and credit score as manually selected inputs.
- Deep learning usually learns features automatically from raw data. It can discover patterns in images, sound, or text without the same level of manual preparation.

### 2. Data requirements
- Traditional machine learning can often work well with smaller, structured datasets.
- Deep learning usually needs much larger amounts of data to perform well because it is learning many internal parameters.

### 3. Model complexity
- Traditional machine learning models are often simpler and more compact.
- Deep learning models are usually more complex, with many layers and many parameters.

### 4. Interpretability
- Traditional machine learning models are often easier to explain. A decision tree or logistic regression model can show which factors mattered most.
- Deep learning models are often harder to interpret because their internal decision process is distributed across many layers and units.

### 5. Computational cost
- Traditional machine learning generally requires less computing power.
- Deep learning typically needs specialized hardware, such as GPUs, and more time for training.

### 6. Performance on unstructured data
- Traditional machine learning often performs well on structured data like spreadsheets or forms.
- Deep learning is especially strong for unstructured data such as images, audio, video, and natural language.

### 7. Analogy: skilling route vs. raid learning
A useful analogy is to compare traditional machine learning to manually planning a skilling route in Old School RuneScape. A player might decide in advance which skills to train, which quests to do, and which gear to upgrade in a specific order. The plan is based on human reasoning and a clear structure. Deep learning is more like a system that learns from thousands of raid attempts, boss kills, or PvP encounters. Instead of following one prewritten plan, it gradually learns which patterns matter most from repeated experience.

## Example comparison
- Traditional ML: predicting customer churn from a table of known features.
- Deep learning: identifying objects in thousands of images or generating text from language data.

## Prompt notes
Use this section to capture the relationship between neural networks and the broader field of machine learning and deep learning.
