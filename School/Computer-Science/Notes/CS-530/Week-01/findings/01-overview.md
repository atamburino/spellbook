# Overview

## Research focus
This section focuses on the main machine learning model types and how they differ in the kind of data they use, the problems they solve, and the kinds of real-world tasks they support.

## Main idea
Artificial intelligence is the broad field, machine learning is a major subset of it, and deep learning is a specialized subset of machine learning. Within machine learning, there are several major learning strategies, each suited to different kinds of data and different goals.

## Major machine learning model types

### 1. Supervised learning
- Data used: labeled data, meaning the input examples already have the correct output attached.
- Problem it solves: classification and regression tasks, where the goal is to predict a label or value.
- Real-world example: spam detection in email, where messages are labeled as spam or not spam.
- Analogy: In Old School RuneScape, this is like learning a boss fight from a guide where each mechanic is already labeled and explained. You are learning from examples that already have the correct answer.

### 2. Unsupervised learning
- Data used: unlabeled data, where the model is not given correct answers in advance.
- Problem it solves: discovering hidden patterns, clustering similar cases, or identifying unusual data points.
- Real-world example: customer segmentation, where a company groups customers based on similar behavior without predefined categories.
- Analogy: In World of Warcraft, this is like studying the auction house and noticing which items tend to move together or which players behave similarly without being told what groups to look for.

### 3. Semi-supervised learning
- Data used: a small amount of labeled data plus a larger amount of unlabeled data.
- Problem it solves: situations where labels are expensive or slow to obtain, but plenty of raw data is available.
- Real-world example: medical image analysis, where a few images are labeled by experts but many more are not.
- Analogy: In Old School RuneScape, this is like learning a skill with a few trusted guides and then practicing many times on your own. You use a little guidance plus a lot of experience.

### 4. Reinforcement learning
- Data used: observations, actions, and feedback in the form of rewards or penalties over time.
- Problem it solves: sequential decision-making, where the system learns by trial and error.
- Real-world example: robotics, game-playing agents, or optimization systems that learn how to make better choices over repeated attempts.
- Analogy: In World of Warcraft, this is like learning PvP or raid play by trying different strategies, getting rewarded for good decisions, and being punished for mistakes. The system improves through feedback.

### 5. Generative models
- Data used: large collections of examples that allow the model to learn patterns and structure.
- Problem it solves: creating new content that resembles the training examples, such as text, images, audio, or code.
- Real-world example: large language models that generate text, or image generators that create new visuals from learned patterns.
- Analogy: In Old School RuneScape or World of Warcraft, this is like a quest writer or NPC dialogue designer who studies many existing quest lines or conversations and then generates new content that feels consistent with the world.

## Working notes
- These model types are not just different algorithms; they reflect different assumptions about the data and the problem.
- Supervised learning works when labels exist.
- Unsupervised learning works when the goal is to discover structure without labels.
- Reinforcement learning works when the system must act over time and learn from consequences.
- Generative models work when the goal is to create something new rather than only classify or predict.

## Analogy caution
These game analogies help with intuition, but they do not fully capture the technical details. A model does not think or plan the way a player does; it learns statistical patterns from data.
