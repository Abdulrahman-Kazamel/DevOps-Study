Db Context class , is a class file that acts as a bridge between entity framework core and the data base. Using this class we will be able to talk to tables of the database from our application.

Add-Migration ==> it creates the Database tables based on our ApplicationDbContext class, which tells the database though the DBset, to create a collection of entity as entities and all the data table is coming from that entity properties. 




// IEnumerable (قراءة فقط)
IEnumerable<int> nums = new List<int> { 1, 2, 3 };

// ICollection (يمكن تعديل القائمة لكن بدون فهرسة)
ICollection<int> nums2 = new List<int> { 1, 2, 3 };
nums2.Add(4);

// IList (تعديل + فهرسة)
IList<int> nums3 = new List<int> { 1, 2, 3 };
nums3[0] = 10;

// HashSet (لا يسمح بالتكرار)
HashSet<string> tags = new HashSet<string> { "c#", "mvc", "c#" }; // سيتم حذف التكرار تلقائيًا

// Dictionary (key-value)
Dictionary<int, string> users = new Dictionary<int, string>();
users.Add(1, "Ahmed");
users.Add(2, "Sara");
-------------
back to migration zero even after applied to database
update-database -migration:0
then remove migration

back to specific migration 
update-database 2021444MigrationNumber



3 ways of considering domain model as table ==>
1- prop of type dbset<>
2- through the modelbuilder.enitity<myModelName>
3- if I have navigation to another model inside my any of models inside the dbset


@Html.DropDownListFor(m => m.Movie.GenreId, new SelectList(Model.category, "Id", "Name"))



# Roadmap

## Foundational Level 1: Programming, OOP, & DSA (6-12 Months)
This initial phase is crucial. It's like building the foundation of a house; skipping it will lead to instability later on.

### Programming Languages (e.g., Rust, C++, C#, Java, Python)
#### Structured Programming
- [ ] Data Types
- [ ] Variables
- [ ] Operators
- [ ] Conditional Statements (if, switch)
- [ ] Looping Constructs (for, while)
- [ ] Functions
- [ ] Structs
#### Object-Oriented Programming (OOP) Paradigm
- [ ] Inheritance
- [ ] Encapsulation
- [ ] Abstraction
- [ ] Polymorphism

### Data Structures

#### Linear
- [ ] Array, Dynamic Array
- [ ] Linked List
- [ ] Stack
- [ ] Queue
#### Non-Linear
- [ ] Tree (specifically Binary Search Tree)
- [ ] Dictionary (Set, Hash Table)
- [ ] Graph

### Algorithms

#### Searching
- [ ] Binary Search
- [ ] Linear Search
#### Sorting
- [ ] Bubble Sort
- [ ] Quick Sort
- [ ] Merge Sort
#### Graph Traversal
- [ ] BFS (Breadth-First Search)
- [ ] DFS (Depth-First Search)
#### Other Techniques
- [ ] Backtracking and Recursion
- [ ] Greedy Algorithms
- [ ] Dynamic Programming

### Problem Solving (on platforms like LeetCode/HackerRank)
- [ ] Easy: 50-100 problems
- [ ] Medium: 15-40 problems

*Projects*

- [ ] Build a small project to apply what you've learned (e.g., a management system for a pharmacy, HR, or school, or games like Snake and Pong).

This entire phase should take approximately *6-12 months* to complete thoroughly.

---

## Foundational Level 2 (Ideal Path): Core CS Principles
These subjects can be studied in parallel and don't always require immediate practical application. For guidance, check university course maps, such as the [CS Course Map Guides from UC Berkeley]( https://hkn.eecs.berkeley.edu/courseguides ).

### Operating Systems
### Databases
### Networking
### Software Engineering (e.g., Agile methodologies)

---

## Foundational Level 3: Track/Domain Fundamentals
Focus on understanding the core principles of your chosen specialization (e.g., web, mobile, game development). Crash courses are a great way to get an introduction to a domain.

---
## Foundational Level 4: Track/Technology
Choose specific technologies within your domain (e.g., .NET, Flutter, Node.js). This choice should be based on your domain's fundamentals and personal interest, not just on current popularity.

---
## Entering the Job Market
- Build a *strong portfolio* to showcase your work.
- Focus on gaining practical experience through **internships and personal projects**.
- Prepare for interviews by practicing and demonstrating your **practical understanding**.
- Remember that *continuous learning* is essential in the tech field.
- Your *passion and a strong foundation* are more critical than chasing trends.
- Refer to this video for more guidance: [Career Options]( https://www.youtube.com/live/1EsfJqxG3Xs )

---
## Different Learning Paths
- **Perfect Path**: Study all four foundational levels for a robust and adaptable career. This is the ideal approach for long-term success.
- *Quick Path**: Focus on the **first foundational level* and then jump to a specific **technology/domain**. It is crucial to return to the second and third levels after get a job to build a stronger career foundation.

- the roadmap on github https://github.com/ramadan-x/roadmap








