# Crystal
Not to be confused with [NinXout's Crystal Client](https://github.com/ninXout/Crystal-Client)

Crystal is a programming language that is similar to python, 'Hello World!' Example:
```crystal
log('Hello World!')
```

You can make your own libs but all libs must contain:
```python
class Actions:
  def yourAction():
    print('Hello World!') # this is an example, you can change the function name and its actions to anything you want
actions = {
  'youraction': Actions.yourAction, # also an example, you can change the command name or add more functions
}
```
`Actions class` and `Actions variables` are required
