using System;
namespace StrategyDesingPattern
{
  class Program
  {
    static void Main(string [] args){
      ZipCompression zipComp = new ZipCompression();
      CompressionContext ctx = new CompressionContext(zipComp);
      ctx.CreateArchive("DoNetDesignPattern");

      ZipCompression rarComp = new RarCompression();
      CompressionContext ctx = new CompressionContext(rarComp);
      ctx.CreateArchive("DoNetDesginPatter");

      Console.Read();
    }
  }
}