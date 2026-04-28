
SOLID = **S**ingle Responsibility, **O**pen/Closed, **L**iskov Substitution, **I**nterface Segregation, **
D**ependency Inversion. 
These five principles help make OOP code more maintainable, testable and extensible.


## [[S — Single Responsibility Principle (SRP)]]

> [!note] Definition  
> A class should have **one and only one reason to change** — one responsibility. (Applied to classes/modules.)

**Why:** Keeps code simple, easier to test and change safely.
>[!example] Typical violation & refactor (Invoice)


```c#

// BAD: single class doing many things
class Invoice
{
    public decimal Amount { get; set; }
    public void CalculateTotal() { /* calculate */ }
    public void PrintInvoice() { /* print to console / printer */ }
    public void SaveToDatabase() { /* persist */ }
}


// BETTER: separate responsibilities
class Invoice { public decimal Amount { get; set; } }
class InvoicePrinter { public void Print(Invoice i) { /* print logic */ } }
class InvoiceRepository { public void Save(Invoice i) { /* DB logic */ } }


```

**Notes / Tips**

- If a class mixes domain logic + I/O + persistence + formatting → split it.
    
- Each class should be small and focused so tests are clear and cheap



## [[O — Open / Closed Principle (OCP)]]

> [!note] Definition  
> Software entities (classes, modules, functions) should be **open for extension** but **closed for modification** — extend behavior without changing existing code.
> as Its tested many times 


> [!example] Shapes + area calculation 


```c#
// BAD: modify existing switch to add new shape
public double Area(object shape)
{
    if (shape is Circle c) return Math.PI * c.Radius * c.Radius;
    if (shape is Rectangle r) return r.Width * r.Height;
    // adding Square requires editing this method — violation
}

// BETTER: use polymorphism
abstract class Shape { 
public abstract double Area(); 
}
class Circle : Shape 
{ 
 public double Radius;
 public override double Area() => Math.PI * Radius * Radius;
 }
class Rectangle : Shape 
{ 
 public double Width, Height; 
 public override double Area() => Width * Height;
 }

// Now client code calls shape.Area() — new shapes don't modify existing code.

```

**How to apply**

- Prefer composition / strategy / polymorphism.
    
- Use abstractions (interfaces/abstract classes) to let new behavior plug in.
## [[L — Liskov Substitution Principle (LSP)]]

> [!note] Definition  
> Subtypes must be replaceable for their base types **without breaking behavior** — derived classes should honor contracts (no surprising behavior). 

> [!example] Rectangle / Square classic problem



```c#
class Rectangle
 { 
	public virtual int Width { get; set; } 
	public virtual int Height { get; set; } 
	    
	public int Area() => Width * Height;

 }

class Square : Rectangle
{
    public override int Width { set { base.Width = base.Height = value; } }
    public override int Height { set { base.Width = base.Height = value; } }
}

// Using Square where Rectangle expected may break code that assumes Width & Height can differ.



```

**How to think about LSP**

- If a derived class cannot fully satisfy all expectations (preconditions, postconditions, invariants) of the base, it breaks LSP.
    
- Solutions: redesign hierarchy, prefer composition over inheritance, or split responsibilities into interfaces


```C#
also as diffrent way , when we need to fire some types of emplyees and exclue another as CEO,

we should create that type which inhirtes from the Empolyee then those type inhirtit from it.

and the type we want to  exclude as CEO , we lit him inhirit from the employee directirtly
```




## [[I — Interface Segregation Principle (ISP)]]

> [!note] Definition  
> Clients should **not** be forced to depend on interfaces they do not use. Create small, role-specific interfaces rather than one large interface

> [!example] Printer device


```c#

// BAD: fat interface
interface IMultiFunctionDevice
{
    void Print(Document d);
    void Scan(Document d);
    void Fax(Document d);
}

// If a simple printer cannot fax/scan, it must implement unused methods.


// BETTER: split interfaces
interface IPrinter { void Print(Document d); }
interface IScanner { void Scan(Document d); }
interface IFax { void Fax(Document d); }

// compose as needed
class BasicPrinter : IPrinter { public void Print(Document d) { /*...*/ } }
class AllInOne : IPrinter, IScanner, IFax { /* implement all */ }


```

**Why it matters**

- Smaller interfaces reduce coupling and make implementations simpler and more testable
## [[D — Dependency Inversion Principle (DIP)]]

> [!note] Definition  
> High-level modules should **not depend** on low-level modules. Both should depend on **abstractions**. Abstractions should not depend on details; details depend on abstractions. 

> [!example] Notification sender (Email/SMS)


```c#
// BAD: high-level depends on concrete low-level
class ReportGenerator
{
    private EmailSender _email = new EmailSender(); // tight coupling
    public void Generate() { /*...*/ _email.Send("done"); }
}

// BETTER: depend on abstraction
interface IMessageSender { void Send(string message); }
class EmailSender : IMessageSender { public void Send(string m) { /* send email */ } }
class SmsSender : IMessageSender { public void Send(string m) { /* send sms */ } }

class ReportGenerator
{
    private readonly IMessageSender _sender;
    public ReportGenerator(IMessageSender sender) { _sender = sender; } 
    // inject abstraction
    public void Generate() { /*...*/ _sender.Send("done"); }
}

```

**Notes**

- Use Dependency Injection to provide concrete implementations at runtime.

- Helps testing: you can pass a mock IMessageSender.



## Summary

```C
- S: Single Responsibility — one reason to change.
- O: Open/Closed — open for extension, closed for modification.
- L: Liskov Substitution — subtypes must be replaceable for base types.
- I: Interface Segregation — small, role-specific interfaces.
- D: Dependency Inversion — depend on abstractions, not concretions.

```