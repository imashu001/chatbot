# Chatbot Learning Roadmap

Build one chatbot in stages. Each project adds a small number of new ideas, so the code grows from a simple conversation loop into a reliable, useful AI assistant.

## Project 01: Command-Line Chatbot

**What you build:** A terminal chatbot that sends a user message to an LLM and prints the response.

**Features to build:**

- A clear input and response loop
- A system prompt that defines the assistant's behavior
- A configurable model and API key loaded from environment variables
- Friendly handling for empty input, exit commands, and API errors
- A clean project structure with a `README`, dependency file, and `.env.example`

**Core concepts learned:** API requests, messages and roles, environment variables, exceptions, and basic application structure.

**Why it is easy:** There is no memory or database yet. The focus is understanding the request-response cycle.

## Project 02: Streaming Chatbot

**What you build:** An improved terminal chatbot that displays the answer as it is generated instead of waiting for the complete response.

**Features to build:**

- Token-by-token or chunked streaming output
- A visible thinking/loading state
- Graceful interruption with `Ctrl+C`
- Response timing and token usage information
- A small configuration menu for model and temperature

**Core concepts learned:** Streaming responses, generators or async iteration, terminal output, and latency measurement.

**Why it is easy to moderate:** The chatbot still has no long-term state, but the user experience becomes more interactive.

## Project 03: Chatbot with Persistent Memory

**What you build:** A terminal assistant that remembers conversations after the program closes.

**Features to build:**

- Conversation history stored in JSON first, then SQLite
- Multiple named conversations
- Commands such as `/new`, `/list`, `/switch`, `/clear`, and `/export`
- Automatic timestamps and message IDs
- A sliding context window that keeps prompts within the model limit
- A way to delete or reset saved data

**Core concepts learned:** Conversation history management, context windows, sliding-window truncation, CRUD operations, and data serialization.

**Why it is moderate:** You must manage state consistently and send the right previous turns with every API call.

## Project 04: Personal PDF Q&A Assistant (Basic RAG)

**What you build:** An app where a user uploads a PDF, asks questions, and receives answers grounded in that document with citations.

**Features to build:**

- PDF text extraction with page numbers
- Text cleaning and configurable chunking with overlap
- Local embedding generation
- A vector store such as Chroma or FAISS
- Similarity search for the most relevant chunks
- Answers that cite the source page and say when the document does not contain the answer
- A command to rebuild or inspect the document index

**Core concepts learned:** Text processing pipelines, embeddings, cosine similarity, vector stores, naive retrieval-augmented generation, and prompt grounding.

**Why it is moderate:** This combines file processing, semantic search, storage, and carefully constrained prompting.

## Project 05: Multi-Document Knowledge Base

**What you build:** A searchable knowledge base that can answer questions across PDFs, Markdown files, text files, and web pages.

**Features to build:**

- A document ingestion pipeline with file type validation
- Metadata for title, source, page, section, and upload date
- Incremental indexing so unchanged files are skipped
- Filters such as “search only this folder” or “search only PDFs”
- Duplicate detection and document deletion
- Citations that link back to the original source
- A command-line or web dashboard showing indexed documents

**Core concepts learned:** ETL pipelines, metadata filtering, indexing strategies, source attribution, and maintainable data boundaries.

**Why it is moderate to hard:** Retrieval quality now depends on both the content and the metadata around each chunk.

## Project 06: RAG Evaluation and Improvement Lab

**What you build:** A test harness that measures whether retrieval and generated answers are actually useful.

**Features to build:**

- A small dataset of questions, expected sources, and reference answers
- Retrieval precision and recall checks
- Groundedness and answer relevance scoring
- Comparison of chunk sizes, overlap, embedding models, and top-k values
- A script that produces a repeatable evaluation report
- Logging of prompts, retrieved chunks, latency, and token cost

**Core concepts learned:** Evaluation datasets, experiment design, observability, retrieval tuning, and regression testing for AI behavior.

**Why it is hard:** “It seems to work” is no longer enough; you need evidence for every improvement.

## Project 07: Tool-Using Personal Assistant

**What you build:** A chatbot that can choose safe tools to complete tasks instead of only generating text.

**Features to build:**

- A calculator and date/time tool
- Local notes and task-list tools
- Search over the user's knowledge base
- Structured tool schemas and validated arguments
- Confirmation before destructive or external actions
- Clear display of tool calls, results, and failures
- A permission setting that enables or disables each tool

**Core concepts learned:** Function calling, structured outputs, tool routing, validation, permissions, and human-in-the-loop workflows.

**Why it is hard:** The model can now cause side effects, so correctness and safety matter as much as answer quality.

## Project 08: Conversation Summaries and Long-Term Memory

**What you build:** A chatbot that remembers useful facts without sending the entire conversation on every request.

**Features to build:**

- Automatic summaries when a conversation becomes long
- Separate short-term conversation memory from long-term user facts
- User controls to view, edit, or delete remembered facts
- Semantic search over previous conversations
- Memory confidence and source references
- Rules that prevent secrets or sensitive data from being saved accidentally

**Core concepts learned:** Hierarchical memory, summarization, semantic recall, privacy controls, and memory lifecycle management.

**Why it is hard:** The assistant must decide what is worth remembering and must remain correct when old information changes.

## Project 09: Production-Ready Chatbot Web App

**What you build:** A polished web application with accounts, a chat interface, document uploads, and persistent user data.

**Features to build:**

- Responsive chat UI with streaming responses
- User authentication and isolated conversations
- Document upload, indexing status, and source previews
- Conversation search, rename, export, and deletion
- Rate limiting, request timeouts, retries, and structured logging
- Background jobs for document ingestion
- Database migrations and automated backups
- Unit, integration, and end-to-end tests

**Core concepts learned:** Frontend and backend integration, authentication, asynchronous jobs, API design, testing, security, and deployment.

**Why it is advanced:** Many users, failures, and workflows must work reliably at the same time.

## Project 10: Agentic Research Assistant

**What you build:** An assistant that turns a complex question into a plan, gathers information from approved sources, checks its work, and produces a cited report.

**Features to build:**

- Planning and task decomposition
- Controlled web or database search
- Parallel research tasks with a maximum step and time limit
- Source quality checks and citation tracking
- A review pass that finds unsupported claims
- Resumable jobs and progress updates
- Full traces for debugging every decision and tool call
- Approval gates before publishing or taking external actions

**Core concepts learned:** Agent loops, orchestration, state machines, concurrency, verification, traceability, and operational safety.

**Why it is the hardest:** The system must coordinate multiple uncertain steps while staying bounded, transparent, and trustworthy.

## Recommended Build Order

1. Make one message work.
2. Make the response feel immediate with streaming.
3. Persist conversations and control the context window.
4. Add one document and grounded citations.
5. Expand to a searchable multi-document knowledge base.
6. Measure retrieval and answer quality before optimizing it.
7. Add tools with strict validation and confirmation.
8. Add summaries and user-controlled long-term memory.
9. Ship the assistant as a tested web application.
10. Orchestrate research only after the simpler pieces are reliable.

## Definition of Done for Every Project

- The feature works from a clean setup using documented commands.
- Configuration and secrets are kept out of source control.
- Invalid input and service failures produce useful error messages.
- At least one happy-path test and one failure-path test exist.
- Logs contain enough context to debug a failed request without exposing private data.
- The README records what was learned and what the next project adds.

