```c#
   ViewBag.ProductLines = productLineRepository.GetAll()
   .Select(r => new  SelectListItem {
         Text = r.Name, 
         Value = r.Id.ToString() 
    }).OrderBy(x => x.Text).ToList();
```


```html
 <select name="ProductLine" id="ProductLine" asp-for="ProductLine" 
 asp-items="@ViewBag.ProductLines">
    <option value="0">Select One...</option>
    </select>
```