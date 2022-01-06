namespace StrategyDesingPattern
{
  public class CompressionContext {
    private ICompression Compression;

    public CompressionContext(ICompression compression){
      this.Compression = Compression;
    }

    public void SetStrategy(ICompression compression){
      this.Compression = compression;
    }

    public void CreateArchive(string compressedArchiveFileName){
      Compression.CompressFolder(compressedArchiveFileName);
    }
  }
}