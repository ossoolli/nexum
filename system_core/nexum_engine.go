package main

import (
    "fmt"
    "net/http"
    "io/ioutil"
)

func main() {
    fmt.Println("🔱 NEXUM Go-Engine: Initializing...")
    resp, err := http.Get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
    if err != nil {
        fmt.Println("❌ Error fetching from Binance")
        return
    }
    body, _ := ioutil.ReadAll(resp.Body)
    fmt.Printf("📊 Real-time Feed: %s\n", string(body))
}
