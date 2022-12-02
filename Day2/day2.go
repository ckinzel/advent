func main() {
    content, err := os.ReadFile("day2in.txt")
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(string(content))
}