# Making a UI Model

## The idea

Imagine an enterprise tool that turns a designer's request into a working prototype built with the company's real frontend library.

The designer might ask:

> Make a claims dashboard with a filter panel, summary cards, and an accessible results table.

The tool should:

- use approved components and design tokens;
- follow the correct business unit's patterns;
- generate runnable code;
- avoid inventing component properties;
- pass accessibility and code checks; and
- show a visual preview.

This is best understood as an **AI system**, not merely one custom model. An AI system can combine a language model, document retrieval, rules, tools, validators, and ordinary application code. The course describes AI as the broad field, ML as one AI domain, and deep learning as complex models within ML. [Course source: Chapter 1, pp. 1-2 and 72-78](../sources/chapter-1.pdf#page=1)

## The answer in one picture

```text
Designer request
      |
      v
Retrieve the right design-system documentation
      |
      v
Language model generates a structured UI plan and code
      |
      v
Ordinary software validates components, types, tests, and accessibility
      |
      v
Browser renders the prototype
      |
      v
Visual and automated evaluation decides whether it passes
```

The language model is important, but the surrounding system makes its output trustworthy.

## Kindergarten version: the LEGO workshop

Think of your frontend library as a company LEGO set.

- **Components** are approved bricks.
- **Design tokens** are approved colors, spacing, and sizes.
- **Documentation** is the instruction book.
- **Examples** are finished LEGO kits.
- **The language model** is a builder that has learned general building patterns.
- **Retrieval** places the correct instruction pages on the table for this job.
- **Fine-tuning** gives the builder repeated practice producing your preferred kind of result.
- **Validators and tests** reject builds that use fake bricks or fall apart.
- **The complete AI system** is the whole workshop, not just the builder.

### Where the analogy breaks

An LLM does not retrieve a perfectly remembered instruction from its weights. Its parameters represent learned numerical patterns. It can still produce plausible but invalid code. That is why the workshop needs current documents and mechanical checks outside the model. Neural-network training adjusts weights to reduce error; it does not create human memory or understanding. [Course source: Chapter 1, pp. 48-54](../sources/chapter-1.pdf#page=48)

## First: fix four easy misconceptions

### 1. Deep learning is not added on top of machine learning

Deep learning **is a type of machine learning**. A transformer language model is a deep neural network trained with machine-learning methods. [Course source: Chapter 1, pp. 1-2 and 76-78](../sources/chapter-1.pdf#page=2)

Incorrect picture:

```text
some ML + some deep learning = UI model
```

Better picture:

```text
AI system
├── deep-learning language model (this is ML)
├── retrieval/search
├── rules and normal code
├── build and browser tools
└── tests and evaluations
```

### 2. Business units are not neural-network layers

A neural-network layer is a mathematical transformation inside the network. It is not a folder or department. Business-unit separation would normally happen through metadata, access controls, separate document collections, prompts, evaluations, or separate fine-tuning adapters. The textbook uses layers to describe connected artificial neurons and learned transformations. [Course source: Chapter 1, pp. 16-18 and 48-50](../sources/chapter-1.pdf#page=16)

### 3. An open-weight model is not a model architecture

**Open weight** describes what is released and how it may be used. It does not mean transformer, deep learning, UI model, or locally trained model. Open weights are downloadable learned parameters. [Open Source Initiative: Open Weights](https://opensource.org/ai/open-weights)

You could:

- use someone else's open-weight base model privately;
- fine-tune that model and keep the new adapter private;
- publish only your adapter if its license and company policy allow it; or
- publish your resulting weights, training code, and permitted data information.

Enterprise UI code and design material may be confidential or licensed. Calling the result “open weight” would mean releasing learned weights outside the company; it does not merely mean running the model on company hardware. The Open Source Initiative also distinguishes open weights from the broader requirements of open-source AI. [OSI: Open Source AI Definition 1.0](https://opensource.org/ai/open-source-ai-definition)

### 4. The model predicts tokens, not necessarily characters

A causal language model predicts the next **token** from earlier tokens. A token can be a word, part of a word, punctuation, or code fragment. Repeating this prediction generates text or code. [Hugging Face: Causal language modeling](https://huggingface.co/docs/transformers/en/tasks/language_modeling)

The next-token prediction is not a separate traditional-ML component beside deep learning. It is the learning objective used to train the deep-learning language model.

## What are we actually trying to build?

Before choosing a model, define the target:

> Given a natural-language request and an approved business-unit context, generate a valid prototype using only approved components and patterns, then prove that it builds, renders, and passes agreed checks.

That target contains several smaller tasks:

| Subtask | Likely solution |
| --- | --- |
| Understand the request | Language model |
| Find current component knowledge | Retrieval/search |
| Select allowed business-unit material | Metadata filters and access control |
| Plan the page | Language model plus schema |
| Generate code | Language model |
| Reject fake component APIs | Type checker, linter, component manifest |
| Check behavior | Unit and browser tests |
| Check appearance | Screenshot comparison or human review |
| Learn whether it is improving | Evaluation dataset and metrics |

This is why “Which model should we train?” is not the first question. The first question is “What must the complete system do, and how will we measure it?” OpenAI's model-optimization guidance places evaluations, prompting/context, and fine-tuning inside an iterative optimization cycle. [OpenAI: Model optimization](https://developers.openai.com/api/docs/guides/model-optimization)

## The three ways to teach the system company knowledge

### Method 1: Put instructions in the prompt

Give the model a compact set of rules and examples with each request.

```text
Use only components listed in the supplied manifest.
Return a UI plan before returning code.
Never invent component properties.
```

This is the fastest experiment. It does not change the model's weights.

**Use it for:** behavior that can be expressed in short, stable instructions.

### Method 2: Retrieval-augmented generation (RAG)

Store component documentation, tokens, examples, and policies in a searchable knowledge collection. For each request, retrieve only the relevant pieces and give those pieces to the model.

```text
All company knowledge
      |
      v
Search for "claims table + filters + accessibility"
      |
      v
Small relevant context
      |
      v
Model response
```

Retrieval systems commonly use vector stores: files are split into chunks, embedded as numerical representations, and searched for relevant content. [OpenAI: Retrieval](https://developers.openai.com/api/docs/guides/retrieval)

**Use it for:** facts that are large, private, frequently changing, or need source citations.

This is probably the first strong fit for your design system. Component APIs change. Retrieval lets the model consult the current instructions without retraining every time a button property changes.

### Method 3: Fine-tuning

Fine-tuning continues training a pretrained model on curated examples so some of its weights - or added adapter weights - change.

Example pair:

```text
Input:
Create a claims-search page for Business Unit A.

Desired output:
1. A valid structured plan
2. Approved component names
3. Correct TypeScript implementation
4. Required tests
```

**Use it for:** repeated behavior, format, style, or domain patterns that prompting and retrieval do not teach reliably enough.

Fine-tuning is not the best storage system for frequently changing component facts. Those facts are easier to update and audit in retrieval documents.

## The practical answer: use all three at different jobs

```text
Prompt       = rules for this run
Retrieval    = current company knowledge
Fine-tuning  = practiced behavior
Tests        = proof that the output works
```

### WoW version

- **Prompt:** Today's raid instructions.
- **Retrieval:** Opening the correct boss guide.
- **Fine-tuning:** Months of practicing your rotation.
- **Tests:** The damage meter and whether the boss actually died.

The raid guide should not be permanently memorized if the boss mechanics change next Tuesday. Likewise, changing component documentation belongs in retrieval before it belongs in training.

## A realistic step-by-step path

### Step 1: Pick one tiny use case

Start with one business unit and one page type.

Example:

> Generate a searchable results page using five approved components.

Do not begin with every business unit, every workflow, and every frontend repository.

### Step 2: Define what “correct” means

Create 20-50 representative tasks before changing a model. Keep expected properties for each task.

Possible checks:

- project builds;
- TypeScript has no errors;
- only approved components appear;
- no invented properties appear;
- accessibility checks pass;
- correct business-unit tokens appear;
- required interaction works; and
- a designer accepts the visual result.

An evaluation dataset makes model and system comparisons repeatable instead of depending on whether one demo looked impressive. OpenAI's eval guidance recommends representative test data and task-specific graders. [OpenAI: Working with evals](https://developers.openai.com/api/docs/guides/evals)

### Step 3: Build a clean knowledge package

Collect only approved, useful sources:

- component names and properties;
- design tokens;
- Storybook documentation;
- good production examples;
- accessibility rules;
- page templates;
- business-unit variations;
- deprecated patterns; and
- examples of what **not** to generate.

Remove secrets, customer information, generated junk, duplicate examples, and code the enterprise does not have permission to use for this purpose.

### Step 4: Make the data machine-readable

Do not throw an entire repository into every prompt. Create small records with metadata.

```yaml
component: ResultsTable
business_unit: claims
version: 3.2
status: approved
source: packages/claims-ui/src/ResultsTable.tsx
allowed_props:
  - columns
  - rows
  - loading
accessibility_notes:
  - Every column needs a visible label.
```

Metadata makes it possible to retrieve only approved content for the selected business unit.

### Step 5: Establish a baseline with an existing model

Use an existing capable coding model with:

- a strong system prompt;
- retrieved design-system records;
- a required output schema;
- access to the build and test tools; and
- the evaluation tasks from Step 2.

Record quality, latency, token use, and cost. This baseline tells you whether a custom model is actually necessary.

### Step 6: Reduce context before training

If cost is driven by giant repeated prompts, fix information flow first:

- retrieve a few relevant records instead of sending the whole library;
- send compact component manifests;
- keep static instructions stable for [prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching) where supported;
- ask for a structured plan before code;
- reuse generated project state instead of resending it; and
- use deterministic tools for facts the model should not guess.

This stage may solve much of the cost problem without changing any weights.

### Step 7: Add a validation loop

The first generated answer is a draft, not the finished prototype.

```text
generate
   |
   v
type-check -> lint -> test -> render -> accessibility check
   |                                      |
   +--------------- failures -------------+
                     |
                     v
               repair attempt
```

The validators are mostly ordinary algorithms and software tools. They do not need ML to know that a TypeScript property does not exist or that a build failed.

This is the connection back to AI: an intelligent application can contain a deep-learning model **and** explicit non-ML algorithms.

### Step 8: Study the failures

Group failures instead of immediately fine-tuning:

- missing knowledge;
- wrong document retrieved;
- unclear instruction;
- invalid component API;
- wrong business-unit style;
- poor visual composition;
- inaccessible markup; or
- model too weak for the task.

Each failure type suggests a different fix. Missing knowledge may require better retrieval. Invalid APIs may require stronger schemas and type checks. Repeated style errors may justify fine-tuning.

### Step 9: Fine-tune an open-weight base only if evidence supports it

Choose an existing open-weight coding-capable base whose license, size, language support, context length, and hardware needs fit the enterprise.

Prepare high-quality training examples from approved inputs and desired outputs. Keep evaluation tasks separate from training data so the test is honest.

For an early experiment, parameter-efficient fine-tuning may be more realistic than changing every parameter. LoRA freezes the base weights and trains smaller update matrices, greatly reducing the number of trainable parameters. [Hugging Face PEFT: LoRA](https://huggingface.co/docs/peft/main/en/package_reference/lora)

Possible structure:

```text
Open-weight base coding model
├── shared company UI adapter
├── Business Unit A adapter
└── Business Unit B adapter
```

This is a possible design, not an automatic requirement. Hugging Face documents that lightweight LoRA adapters can be trained and switched while the original pretrained weights remain frozen. [Hugging Face: Parameter-efficient fine-tuning](https://huggingface.co/docs/transformers/main/peft)

### Step 10: Compare, do not assume

Run the same evaluation set against:

1. frontier model plus retrieval;
2. smaller hosted model plus retrieval;
3. open-weight base plus retrieval; and
4. fine-tuned open-weight model plus retrieval.

Compare:

- valid-build rate;
- approved-component rate;
- accessibility pass rate;
- designer acceptance;
- latency;
- cost per accepted prototype; and
- operational effort.

The winner is the system that meets the enterprise requirement, not the system with the most impressive model label.

### Step 11: Scale business units through governance

Add a business unit only after the first unit works.

For each unit, define:

- authorized data sources;
- approved components and tokens;
- retrieval filters;
- example tasks;
- evaluation thresholds;
- reviewers and owners; and
- release and rollback rules.

Shared foundations can remain common while business-unit knowledge stays separated. This is a data-governance and system-design problem more than a “make the neural network deeper” problem.

## Should we train from scratch?

Probably not for the first versions.

Training from scratch means beginning with mostly random parameters and teaching a model general language, code, reasoning patterns, and then company UI behavior. Adapting a pretrained model begins with capabilities already learned and focuses effort on the enterprise task. The course explains that deep models contain many parameters and became practical through increased compute and data availability. [Course source: Chapter 1, pp. 2 and 76-78](../sources/chapter-1.pdf#page=2)

A reasonable learning ladder is:

1. existing model + prompt;
2. existing model + retrieval + tools;
3. smaller model or open-weight base + the same system;
4. parameter-efficient fine-tuning;
5. full fine-tuning, only if justified; and
6. pretraining from scratch, only with an extraordinary reason and resources.

OpenAI's `gpt-oss` release is an example of pretrained open-weight models that can run on controlled infrastructure and be fine-tuned. It illustrates the type of starting point, not an automatic recommendation for this UI project. [OpenAI: Introducing gpt-oss](https://openai.com/index/introducing-gpt-oss/)

## Capstone play: a Gemma-derived enterprise UI model

This is the more ambitious version of the idea worth saving for later:

> Start with a downloadable Gemma foundation model, specialize its learned weights using authorized enterprise frontend data, and produce a smaller company-controlled model that generates valid prototypes in one design system.

This would be a genuine model-building project. It goes beyond wrapping documents around a hosted model because training changes learned parameters and produces a new adapter or derivative checkpoint. Google explicitly supports modifying Gemma's open weights through fine-tuning. [Google: Gemma model fine-tuning](https://ai.google.dev/gemma/docs/tune)

### What is inherited and what is ours?

| Part | Source |
| --- | --- |
| Transformer architecture | Inherited from Gemma |
| Tokenizer | Usually inherited from Gemma |
| General language and coding ability | Learned during Google's pretraining |
| Original foundation weights | Released by Google |
| UI-domain training records | Created from authorized enterprise material |
| LoRA adapter or modified weights | Produced by our training process |
| Evaluation suite | Created for our UI-generation requirements |
| Serving and validation system | Designed and operated by us |

We would not normally “teach the base architecture.” The architecture is the mathematical blueprint we inherit. We would teach new patterns by adjusting weights inside that blueprint.

```text
architecture = shape of the model
weights      = learned numerical settings inside that shape
training     = process that adjusts those settings
```

### The capstone in one diagram

```text
                    GOOGLE
        Gemma architecture + pretrained weights
                         |
                         v
                  OUR TRAINING PIPELINE
        +-------------------------------------+
        | approved UI code and documentation |
        | input -> desired output examples    |
        | training, validation, and test sets |
        +-------------------------------------+
                         |
                         v
             LoRA adapter or tuned checkpoint
                         |
                         v
                 OUR INFERENCE SERVICE
        prompt -> UI model -> code -> validators
                         |
                         v
                accepted prototype or failure
```

### Kindergarten version: train an experienced builder

Gemma is an experienced LEGO builder. Google already taught the builder language, code, and general problem solving.

Our project does not raise a new builder from birth. It gives the experienced builder a long apprenticeship in our company workshop:

- these are our approved bricks;
- this is how our teams combine them;
- these combinations are wrong;
- this is what a finished claims page looks like; and
- this is how we prove the build is acceptable.

At the end, the builder still has Gemma's general education but has new learned habits for our UI domain.

### Choose a starting Gemma variant

Google publishes pretrained, instruction-tuned, and task-specialized Gemma variants. Instruction-tuned variants are the easiest application baseline; pretrained variants provide a more basic checkpoint for researchers who intend to develop capabilities through additional training. [Google: Run Gemma models](https://ai.google.dev/gemma/docs/run)

A capstone comparison could test:

1. an unmodified instruction-tuned Gemma model;
2. that model with retrieval only;
3. that model with a company UI LoRA adapter; and
4. that model with both the adapter and retrieval.

The experiment should begin with the smallest model that might meet the requirement. Google recommends starting small unless testing has shown that a larger model is necessary, because larger models require more compute. [Google: Run Gemma models](https://ai.google.dev/gemma/docs/run)

### Two different training stages

#### Stage A: continued pretraining - learn the dialect

Continued pretraining gives the existing model more next-token training on approved domain material:

- component source;
- TypeScript declarations;
- Storybook descriptions;
- design-token files;
- accessibility standards; and
- high-quality production examples.

The simple mental model is: “Continue Gemma's reading practice, but now the reading material comes from our frontend domain.”

Possible benefit: the model becomes more familiar with company vocabulary and recurring code patterns.

Possible danger: noisy or repetitive repositories may teach poor patterns, and aggressive training may damage useful general capabilities. These are hypotheses to evaluate, not guaranteed outcomes.

#### Stage B: supervised fine-tuning - learn the job

Supervised fine-tuning uses curated input and desired-output pairs:

```json
{
  "input": {
    "request": "Create a claims results page",
    "business_unit": "claims",
    "constraints": ["approved components only", "keyboard accessible"]
  },
  "desired_output": {
    "plan": ["ClaimsFilter", "ClaimsSummary", "ResultsTable"],
    "code": "...reviewed implementation...",
    "tests": "...required checks..."
  }
}
```

This stage teaches response behavior: how to turn a request into the kind of implementation the enterprise accepts. Google describes Gemma tuning data as inputs paired with expected responses. [Google: Gemma model fine-tuning](https://ai.google.dev/gemma/docs/tune)

### Three levels of weight ownership

#### Level 1: LoRA adapter

```text
frozen Gemma weights + our small trained adapter
```

LoRA freezes the original model and trains smaller added matrices. It reduces the number of trainable parameters and the memory required for experiments. The deployed system normally loads both the base model and adapter. [Google: Fine-tune Gemma with LoRA](https://ai.google.dev/gemma/docs/lora_tuning)

This is the strongest capstone starting point because it demonstrates real weight training without requiring a full-model training budget.

#### Level 2: merged derivative

```text
Gemma weights + our adapter -> one merged checkpoint
```

The resulting artifact can be served like one specialized model. It remains a Gemma model derivative and remains subject to the applicable Gemma license.

#### Level 3: full fine-tune

```text
update all or most Gemma parameters
```

This offers more capacity for change but requires substantially more training memory and compute. Google's tuning guide distinguishes full tuning from parameter-efficient methods and recommends techniques such as LoRA when resources are constrained. [Google: Gemma model fine-tuning](https://ai.google.dev/gemma/docs/tune)

### What the first capstone scope should be

Keep the first research question narrow:

> Can a LoRA-tuned Gemma model generate valid searchable-results pages for one business unit more reliably or cheaply than unmodified Gemma?

Constrain the project to:

- one business unit;
- one frontend framework;
- one design-system version;
- roughly five to ten approved components;
- one page family;
- text-to-code input and output; and
- automated plus human evaluation.

Expansion to other business units becomes future work, not part of the first proof.

### Capstone phases

#### Phase 1: governance and data rights

Document:

- which repositories may be used;
- which licenses apply;
- whether employee and customer data is excluded;
- whether generated weights must remain internal;
- who approves training and distribution; and
- the exact license of the selected Gemma checkpoint.

Google's terms define modifications and models created from Gemma's weights as Model Derivatives and apply conditions to use and distribution. The exact version's license must be reviewed before training or sharing. [Google: Gemma Terms of Use](https://ai.google.dev/gemma/terms)

#### Phase 2: baseline and evaluation set

Build unseen success, failure, and boundary cases before training. Google recommends testing tuned models on requests not specifically used during training. [Google: Gemma model fine-tuning](https://ai.google.dev/gemma/docs/tune)

#### Phase 3: data preparation

Create:

- a cleaned domain corpus for optional continued pretraining;
- reviewed request/response examples for supervised tuning;
- metadata for business unit, component version, and approval status;
- negative examples showing prohibited patterns; and
- separate train, validation, and test splits.

#### Phase 4: first LoRA training run

Freeze Gemma's original weights, train an adapter, record training and validation loss, and save versioned checkpoints. Begin with a small LoRA rank and increase it only when evaluation supports doing so. Google's LoRA tutorial recommends beginning with a small rank for efficient experimentation. [Google: Fine-tune Gemma with LoRA](https://ai.google.dev/gemma/docs/lora_tuning)

#### Phase 5: model and system evaluation

Compare all candidates on the same unseen tasks:

| Measurement | What it answers |
| --- | --- |
| Build-pass rate | Does the code compile? |
| Approved-component rate | Does it use the real library? |
| Invented-property rate | Does it hallucinate APIs? |
| Accessibility pass rate | Does it meet automated checks? |
| Visual acceptance | Would a designer keep the result? |
| General coding regression | Did specialization damage base ability? |
| Latency | How quickly does it respond? |
| Cost per accepted prototype | Is it economically useful? |

#### Phase 6: package and deploy

Save:

- base-model identity and license;
- adapter or merged weights;
- tokenizer and chat template;
- training configuration;
- dataset manifest and provenance;
- evaluation results;
- known limitations; and
- deployment configuration.

Quantization can reduce inference memory by representing weights at lower precision. Google generally recommends choosing the model first, tuning at supported precision, and then evaluating quantized deployment variants. [Google: Run Gemma models](https://ai.google.dev/gemma/docs/run)

#### Phase 7: capstone report

The report could answer:

1. How did retrieval and weight training differ?
2. Did continued pretraining improve domain familiarity?
3. Did supervised tuning improve valid UI generation?
4. Did specialization harm general coding ability?
5. Did LoRA provide enough improvement to justify self-hosting?
6. Which costs moved from vendor usage to infrastructure and operations?
7. What prevented the model or its weights from being publicly released?

### What would make this academically valuable?

The capstone would not merely say, “I fine-tuned Gemma.” It would produce a controlled comparison with a reproducible dataset, documented training choices, unchanged test tasks, quantitative results, limitations, and an honest cost analysis.

The scientific question is not whether the tuned output looks cool. It is whether changing weights caused a measurable improvement over prompting and retrieval alone.

### Capstone definition of done

- A versioned Gemma base is documented.
- Training data has provenance and authorization.
- At least one LoRA adapter is trained.
- Test tasks were not included in training.
- Baseline and tuned models are compared on the same metrics.
- A local or controlled inference endpoint serves the tuned model.
- The report includes quality, cost, privacy, licensing, and limitation findings.
- No claim of “open source” or “open weight” exceeds what was actually released and licensed.

## Would the result be open weight?

Only if you actually release trained weights under terms that allow others to use them.

| Situation | Better description |
| --- | --- |
| Claude or another hosted model plus company documents | Proprietary model-based internal AI system |
| Downloaded open-weight base, no training | Internal system using an open-weight model |
| Open-weight base plus private LoRA adapter | Privately fine-tuned open-weight model |
| Base or merged weights published under a suitable license | Released open-weight model |
| Weights, necessary code, and sufficient data information released under qualifying terms | Potentially open-source AI under the OSI definition |

Do not publish learned weights or adapters trained on enterprise material until legal, security, privacy, architecture, and data owners approve the release.

## Where each class concept appears

| Course concept | UI-model project |
| --- | --- |
| Artificial intelligence | The full prototype-generation system |
| Machine learning | The process that produced or adapts learned models |
| Deep learning | The transformer language model generating plans and code |
| Parameters/weights | Learned numbers inside the model |
| Features/input | Tokens representing the request, retrieved docs, and code context |
| Prediction | Probabilities for the next token |
| Training | Adjusting weights using examples and measured error |
| Model architecture | The transformer's layer structure |
| Open weights | A decision to distribute learned parameters |
| Algorithm without ML | Type checking, lint rules, access filters, and test assertions |
| Evaluation | Measuring whether generated prototypes meet requirements |

## The most important takeaway

There are now two legitimate versions of the idea:

1. **Production-system play:** Start with a capable model, retrieve current company knowledge, constrain generation, and verify the result with ordinary software.
2. **Capstone model-building play:** Start with Gemma's architecture and foundation weights, train an enterprise UI adapter or derivative checkpoint, and measure whether changing weights improves quality or cost.

The capstone does not create a foundation model from random weights. It creates a company-specialized **derivative of a foundation model**. That still includes real deep-learning work: preparing training data, adjusting parameters, tracking loss, saving checkpoints, evaluating unseen tasks, quantizing weights, and serving inference.

## From-memory explanation

Complete this without looking back:

> Our UI generator is an AI ___, not only a model. Its language model uses ___ learning, which is a type of ___. Current component facts belong mainly in ___, while repeated desired behavior may eventually justify ___. Business units are separated with data and governance controls, not neural-network ___.

## Retrieval check

1. Why is deep learning not a separate ingredient beside machine learning?
2. Why should current component documentation usually use retrieval instead of fine-tuning?
3. What would type checking catch better than a language model?
4. What is the difference between running an open-weight model privately and releasing your own open weights?
5. What evidence would justify fine-tuning?
6. Why should the first experiment cover one business unit and one page type?
7. What role could a LoRA adapter play?
8. Which parts of a Gemma-derived model are inherited, and which parts would we create?
9. What is the difference between continued pretraining and supervised fine-tuning?
10. What evidence would show that changing weights helped more than retrieval alone?

## Sources

### Course source

- zyBooks, *CS-530 Chapter 1*. Local source: [chapter-1.pdf](../sources/chapter-1.pdf). Relevant pages: 1-2, 16-18, 48-54, and 72-78.

### External verification

- [OpenAI: Retrieval](https://developers.openai.com/api/docs/guides/retrieval) - vector stores, chunking, embeddings, and semantic search.
- [OpenAI: Model optimization](https://developers.openai.com/api/docs/guides/model-optimization) - evaluation, prompting, and fine-tuning as an optimization cycle.
- [OpenAI: Working with evals](https://developers.openai.com/api/docs/guides/evals) - repeatable evaluation datasets and graders.
- [OpenAI: Introducing gpt-oss](https://openai.com/index/introducing-gpt-oss/) - pretrained open-weight models, deployment, and customization.
- [Google: Gemma model fine-tuning](https://ai.google.dev/gemma/docs/tune) - tuning workflow, data pairs, PEFT, full tuning, testing, and deployment.
- [Google: Fine-tune Gemma with LoRA](https://ai.google.dev/gemma/docs/lora_tuning) - LoRA mechanics, training resources, and rank selection.
- [Google: Run Gemma models](https://ai.google.dev/gemma/docs/run) - pretrained and instruction-tuned variants, model sizing, and quantization.
- [Google: Gemma Terms of Use](https://ai.google.dev/gemma/terms) - model derivatives and distribution conditions.
- [Hugging Face: Causal language modeling](https://huggingface.co/docs/transformers/en/tasks/language_modeling) - next-token prediction.
- [Hugging Face PEFT: LoRA](https://huggingface.co/docs/peft/main/en/package_reference/lora) - parameter-efficient adaptation using smaller trainable matrices.
- [Hugging Face: Parameter-efficient fine-tuning](https://huggingface.co/docs/transformers/main/peft) - lightweight adapters on pretrained models.
- [Open Source Initiative: Open Weights](https://opensource.org/ai/open-weights) - open-weight definition and limitations.
- [Open Source Initiative: Open Source AI Definition 1.0](https://opensource.org/ai/open-source-ai-definition) - requirements beyond releasing weights alone.

## Verification notes

- External sources were checked on **July 11, 2026**.
- The architecture described here is a learning design, not a production proposal. An enterprise implementation would require security, privacy, legal, accessibility, design-system, platform, and infrastructure review.
- No company data, model, license, budget, or hardware environment was inspected. Specific model selection and cost estimates therefore remain intentionally open.
