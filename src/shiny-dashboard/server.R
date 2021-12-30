library(jsonlite)
library(dplyr)
library(RSQLite)
library(DBI)
library(ggplot2)
library(shiny)

db_get_api_call_data <- function(){
    con <- dbConnect(SQLite(),"/app/api/resources/flask_logs.db")
    data <- dbGetQuery(con, "SELECT timestamp as time_stamp,method,path,status FROM requests")
    dbDisconnect(con)
    return (data)
}

db_get_request_response_data <- function(){
    con <- dbConnect(SQLite(),"/app/api/resources/flask_logs.db")
    data <- dbGetQuery(con, "SELECT request,response FROM requests where status=200 and path='/api/predict' and method='GET'")
    data <- data %>% rowwise() %>% mutate(label = fromJSON(response)$label,prob=fromJSON(response)$prob1)
    dbDisconnect(con)
    return (data)
}


shinyServer(function(input, output) {
    output$graphRequestsBar <-
        renderPlot({
            db_get_api_call_data() %>% 
            ggplot() + geom_bar(aes(x = as.factor(get(input$graphRequestsBarInput))),fill="deepskyblue4") + labs(title='Cantidad de llamados a la API',x = input$graphRequestsBarInput ,y="Cantidad de llamados")
        })
    output$graphRequestsSeries <-
        renderPlot({
            interval <- case_when(
                input$graphRequestsSeriesInput == 'segundos' ~ "%Y-%m-%d %H:%M:%OS",
                input$graphRequestsSeriesInput == 'minutos' ~ "%Y-%m-%d %H:%M",
            )
          db_get_api_call_data() %>% 
            mutate(time_stamp = strptime(time_stamp, format = "%Y-%m-%d %H:%M:%OS")) %>% 
            group_by(date = as.POSIXct(strptime(time_stamp, format = interval))) %>% 
            summarise(n_req = n()) %>% 
            ggplot() + geom_line(aes(x = date, y = n_req),colour="deepskyblue4") + labs(title='Historial de llamados a la API',x = "Tiempo",y="Cantidad de llamados")
        })
    
    output$graphPredictionHistProb <-
        renderPlot({
            db_get_request_response_data() %>% 
            ggplot() + geom_histogram(aes(x = prob),fill="deepskyblue4",bins = input$graphPredictionInput) + labs(title='Distribucion de probabilidad de que haya al menos una muerte',x = "Probabilidad",y="Cantidad de llamados")
        })
    output$graphPredictionBar <-
        renderPlot({
            db_get_request_response_data() %>% 
            rowwise() %>% 
            mutate(value = fromJSON(request)[[input$graphPredictionBarInput]]) %>%
            ggplot() + geom_bar(aes(x = as.factor(label),fill=value)) + labs(title='Cantidad de predicciones de accidentes con muertes vs sin muertes',x = "Resultado de la prediccion",y="Cantidad de llamados")
        })

})
