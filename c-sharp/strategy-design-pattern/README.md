# Strategy Design Pattern

 - [Dot Net Tutorials](https://dotnettutorials.net/lesson/strategy-design-pattern/)

 ## Participant involved in this example

  - Strategy(ICompression): The strategy declares an interface that is going to be implemented by others object.

  - ConcreteStrategy(RarCompression and ZipCompression): These classes implement the  method CompressFolder that was defined by the Strategy(ICompression) interface.

  - Context(CompressionContext): This class has a atribute with a reference to the Strategy(ICompression) object and uses the reference to execute a ConcreteStrategy(either RarComp or ZipComp in this case)


