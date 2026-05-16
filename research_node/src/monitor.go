package main
import (
    "fmt"
    "net/http"
    "time"
)
func checkService(url string) {
    start := time.Now()
    _, err := http.Get(url)
    duration := time.Since(start)
    if err != nil {
        fmt.Printf("🔴 %s is DOWN (Time: %v)\n", url, duration)
    } else {
        fmt.Printf("🟢 %s is UP (Time: %v)\n", url, duration)
    }
}
func main() {
    urls := []string{"http://localhost:8080", "https://google.com", "https://core.telegram.org"}
    fmt.Println("🚀 Go-Agent: Checking all systems in parallel...")
    for _, url := range urls {
        go checkService(url)
    }
    time.Sleep(2 * time.Second)
}
