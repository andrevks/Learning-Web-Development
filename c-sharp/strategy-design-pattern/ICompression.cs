namespace StrategyDesignPattern
{
  public interface ICompression
  {
    //Declares an interface that is common
    //to all supported algorithms
    void CompressFolder(string compressedArchiveFileName);
  }
}