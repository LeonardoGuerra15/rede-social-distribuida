package main

import (
    "encoding/json"
    "net/http"
    "sync"
    "fmt"
)

type Servidor struct {
    Nome string
    Hora float64
}

var (
    servidores = make(map[string]float64)
    mux sync.Mutex
)

func registrarHandler(w http.ResponseWriter, r *http.Request) {
    var srv Servidor
    json.NewDecoder(r.Body).Decode(&srv)
    mux.Lock()
    servidores[srv.Nome] = srv.Hora
    mux.Unlock()
    w.WriteHeader(http.StatusOK)
    w.Write([]byte("{\"msg\": \"Registrado\"}"))
}

func berkeleyHandler(w http.ResponseWriter, r *http.Request) {
    mux.Lock()
    defer mux.Unlock()
    var soma float64
    for _, h := range servidores {
        soma += h
    }
    media := soma / float64(len(servidores))
    for k := range servidores {
        servidores[k] = media
    }
    json.NewEncoder(w).Encode(servidores)
}

func horasHandler(w http.ResponseWriter, r *http.Request) {
    mux.Lock()
    defer mux.Unlock()
    json.NewEncoder(w).Encode(servidores)
}

func relogioLogicoHandler(w http.ResponseWriter, r *http.Request) {
    type Req struct {
        Relogio int `json:"relogio"`
    }
    var req Req
    json.NewDecoder(r.Body).Decode(&req)
    resp := map[string]int{"relogio": req.Relogio + 1}
    json.NewEncoder(w).Encode(resp)
}

func main() {
    http.HandleFunc("/registrar", registrarHandler)
    http.HandleFunc("/berkeley", berkeleyHandler)
    http.HandleFunc("/horas", horasHandler)
    http.HandleFunc("/relogio_logico", relogioLogicoHandler)
    fmt.Println("Servidor Go rodando na porta 8080")
    http.ListenAndServe(":8080", nil)
}