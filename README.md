Sure! Here's the complete `README.md` content in **one block** — just copy and paste it directly into your `README.md` file:

---

````markdown
# 📊 Spreadsheet API using FastAPI

This project is a simple spreadsheet-like REST API built with **FastAPI** that allows users to set and get values from cells (like `A1`, `B2`, etc.), simulating the behavior of a basic spreadsheet.

---

## 🚀 Features

- 🔢 Set and retrieve values for individual spreadsheet-like cells
- 🌐 Interactive API documentation with Swagger UI (`/docs`)
- 🧠 In-memory data storage using Python dictionary
- ⚡ Fast and lightweight using FastAPI and Uvicorn

---

## 🔧 Requirements

- Python 3.7+
- FastAPI
- Uvicorn

Install dependencies:

```bash
pip install fastapi uvicorn
````

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/SugamaSShetty/spreadsheet-api.git
cd spreadsheet-api
```

2. Run the server using Uvicorn:

```bash
uvicorn main:app --reload
```

3. Open your browser and go to:

```
http://127.0.0.1:8000/docs
```

This opens the Swagger UI to test the API interactively.

---

## 📘 API Endpoints

### ➕ Set Cell Value

```
POST /cells/{cell_id}
```

**Parameters:**

* `cell_id` – Cell name like `A1`, `B2`

**Request Body:**

```json
{
  "value": "100"
}
```

**Example:**

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/cells/A1' \
  -H 'Content-Type: application/json' \
  -d '{"value": "100"}'
```

---

### 📥 Get Cell Value

```
GET /cells/{cell_id}
```

**Parameters:**

* `cell_id` – Cell name like `A1`, `B2`

**Example:**

```bash
curl -X 'GET' 'http://127.0.0.1:8000/cells/A1'
```

---

## 🗂️ Project Structure

```
spreadsheet-api/
├── main.py
├── README.md
└── ...
```

---

## 🧑‍💻 Author

**Sugama S Shetty**
GitHub: [SugamaSShetty](https://github.com/SugamaSShetty)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

````

---

✅ Just create a file named `README.md` inside your project folder, paste the above content, and commit it:

```bash
git add README.md
git commit -m "Added README file"
git push origin main
````

Let me know if you also want a `LICENSE` file or badges like Python version, FastAPI, etc.
