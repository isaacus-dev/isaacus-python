# Embeddings

Types:

```python
from isaacus.types import EmbeddingResponse
```

Methods:

- <code title="post /embeddings">client.embeddings.<a href="./src/isaacus/resources/embeddings.py">create</a>(\*\*<a href="src/isaacus/types/embedding_create_params.py">params</a>) -> <a href="./src/isaacus/types/embedding_response.py">EmbeddingResponse</a></code>

# Classifications

## Universal

Types:

```python
from isaacus.types.classifications.universal import UniversalClassificationResponse
```

Methods:

- <code title="post /classifications/universal">client.classifications.universal.<a href="./src/isaacus/resources/classifications/universal.py">create</a>(\*\*<a href="src/isaacus/types/classifications/universal/universal_create_params.py">params</a>) -> <a href="./src/isaacus/types/classifications/universal/universal_classification_response.py">UniversalClassificationResponse</a></code>

# Rerankings

Types:

```python
from isaacus.types import RerankingResponse
```

Methods:

- <code title="post /rerankings">client.rerankings.<a href="./src/isaacus/resources/rerankings.py">create</a>(\*\*<a href="src/isaacus/types/reranking_create_params.py">params</a>) -> <a href="./src/isaacus/types/reranking_response.py">RerankingResponse</a></code>

# Extractions

## QA

Types:

```python
from isaacus.types.extractions.qa import AnswerExtractionResponse
```

Methods:

- <code title="post /extractions/qa">client.extractions.qa.<a href="./src/isaacus/resources/extractions/qa.py">create</a>(\*\*<a href="src/isaacus/types/extractions/qa/qa_create_params.py">params</a>) -> <a href="./src/isaacus/types/extractions/qa/answer_extraction_response.py">AnswerExtractionResponse</a></code>

# Enrichments

Types:

```python
from isaacus.types import EnrichmentResponse
```

Methods:

- <code title="post /enrichments">client.enrichments.<a href="./src/isaacus/resources/enrichments.py">create</a>(\*\*<a href="src/isaacus/types/enrichment_create_params.py">params</a>) -> <a href="./src/isaacus/types/enrichment_response.py">EnrichmentResponse</a></code>

# ILGS

## v1

Types:

```python
from isaacus.types.ilgs.v1 import (
    Crossreference,
    Date,
    Document,
    Email,
    ExternalDocument,
    IDNumber,
    Location,
    Person,
    PhoneNumber,
    Quote,
    Segment,
    Span,
    Term,
    Website,
)
```
