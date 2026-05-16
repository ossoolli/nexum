package main
import ("fmt"; "net/http"; "io"; "os")
func downloadFile(url string, filepath string) error {
    out, _ := os.Create(filepath)
    defer out.Close()
    resp, err := http.Get(url)
    if err != nil { return err }
    defer resp.Body.Close()
    _, err = io.Copy(out, resp.Body)
    return err
}
func main() {
    fmt.Println("🚀 Scout-Go: Starting Telegram API Doc Harvest...")
    err := downloadFile("https://core.telegram.org/api/pdf", "/home/madarmutaz/AI-Agents/knowledge_base/docs/telegram_api.pdf")
    if err == nil { fmt.Println("✅ Doc Captured.") } else { fmt.Println("❌ Error:", err) }
}
