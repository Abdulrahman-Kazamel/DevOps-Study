============================
Simple Python Task Runner
============================

----------------------------
How it works:
----------------------------
1. Tasks are stored in a SQLite file called `tasks.db`.
2. Each task has:
   - A name
   - A command (like "copy logs.txt" or "read db")
   - A status (pending or done)
3. The program reads tasks marked as "pending" and simulates running them.
4. After each task is completed, it logs the result and marks the task as "done" in the database.

----------------------------
You can extend the project by:
----------------------------
- Adding more tasks to the database
- Supporting new types of commands
- Creating a simple menu to add new tasks via user input

Enjoy building your mini task automation system!
