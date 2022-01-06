using System;
namespace StrategyDesingPattern
{
  public class ZipCompression : ICompression{
    public void CompressFolder(String compressedArchiveFileName){
      Console.WriteLine("Folder is compressed using zip approach:'" +
      compressedArchiveFileName +".zip' file is created ");
    }
  }
}