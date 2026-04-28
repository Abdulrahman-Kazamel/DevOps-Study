-Invalid state: my object holds data against business rules {Encapsulation role Come}

-different signature in {static / method / compile time}  Over Loading Means different (Type of parameters / number of parameters)

-run time over Loading happens with polymorphism in different implementation for the class method.

Abstractions happens in everything around us, ATM, Car start engine, push Benzene.
Abstraction happens in two ways {Abstract class , abstract method}, {using interfaces}
Encapsulation is one of abstraction usage through access modifiers 

Can NOT create Instance of it , derived child able==> also this abstract map is a contract for all.
abstract hide details 

Immutable object {String} : means the object data are set once on the constructor or on the initialization once and not able to be edit and to edit it, I need to create another object, I feel seem as scoped 


difference between abstraction and interface 






# 🧩 OOP Paradigm in C#

## 1. Encapsulation

- **Definition:** Hiding internal state and requiring all interaction through controlled methods (getters/setters).
    
- **Role:** Prevents the object from being in an **invalid state** (data against business rules).
    
- **Tool:** Access Modifiers (`public`, `private`, `protected`, `internal`).
    
- **Example:**
    

```csharp

class BankAccount {   
private decimal balance; // hidden data    

public void Deposit(decimal amount)     {       
	if (amount <= 0) throw new ArgumentException("Invalid amount");    
	balance += amount;    
 }  
   
public decimal GetBalance() => balance; // controlled access }

//==================================== 
class BankAccount
{
    private decimal balance;

    public void Deposit(decimal amount)
    {
        if (amount <= 0) throw new ArgumentException("Invalid amount");
        balance += amount;
    }

    public bool Withdraw(decimal amount)
    {
        if (amount <= 0 || amount > balance) return false;
        balance -= amount;
        return true;
    }

    public decimal Balance => balance; // read-only property
}



```


---

## 2. Abstraction

- **Definition:** Hiding implementation details and showing only essential features.
    
- **Analogy:** ATM → You insert a card & enter a PIN, but don’t know how internal banking systems work.
    
- **In C#:**
    
    - **Abstract classes & methods**         |         **Interfaces**
    
- **Rules:**
    
    - Abstract class: Can’t create an instance. Child classes must implement abstract methods. Can have implemented methods too.
        
    - Interface: Pure contract → defines _what_ must be done, not _how_.
        
- **Example:**
    

``` csharp
abstract class Vehicle 
{  

   public abstract void StartEngine(); // contract   
   public void StopEngine() => Console.WriteLine("Engine stopped"); 
  
 } 

class Car : Vehicle 
{  
 public override void StartEngine() => Console.WriteLine("Car engine started"); 
 }


```



---

## 3. Inheritance

- **Definition:** Mechanism to acquire properties & behaviors of another class.
    
- **Keyword:** `:`
    
- **Example:**

```csharp

class Animal 
{    
 public void Eat() => Console.WriteLine("Eating...");
  } 
 class Dog : Animal 
 {   
   public void Bark() => Console.WriteLine("Barking...");
    }
    
    //when intitaliazing object from Dog Class, it will be able to Eat and Bark

```

---

## 4. Polymorphism

- **Definition:** One interface, many implementations.
    
- **Types in C#:**
    
    - **Compile-time (Method Overloading):** Same method name, different signature (parameter number/parameter type).
    
    - **Run-time (Method Overriding):** Different implementations of the same method in inherited classes.
    
- **Examples:**
    

```c#
// Overloading (compile-time) 
class Calculator {    
 public int Add(int a, int b) => a + b;     
 public double Add(double a, double b) => a + b; 
 }  
 
 // Overriding (run-time) 
 class Shape {   
   public virtual void Draw() => Console.WriteLine("Drawing shape"); }  
  
 class Circle : Shape { 
 public override void Draw() => Console.WriteLine("Drawing circle");
   
 }

```

---

## 5. Immutable Objects

- **Definition:** Once created, state can’t change.
    
- **Example:** `string` in C#
    

```c#
string name = "John"; 
name.Replace("J", "P");
 // actually creates a NEW string "Pohn"

```

- **Custom immutable object:**
    

```c#
class Person {   
 
public string Name { get; }  
   
public Person(string name) => Name = name; 

}
```

---

## 6. Abstraction vs Interface

|**Aspect**|**Abstract Class**|**Interface**|
|---|---|---|
|Instantiation|❌ Cannot create instance|❌ Cannot create instance|
|Implementation|Can have implemented + abstract methods|Only declarations (C# 8+ allows default methods)|
|Inheritance|A class can inherit only **one abstract class**|A class can implement **multiple interfaces**|
|Fields/Constructors|Can have fields, constructors, access modifiers|Cannot have fields/constructors (only properties/methods)|
|Use Case|“is-a” relationship with shared logic|“can-do” behavior contract|

