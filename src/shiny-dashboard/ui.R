library(shiny)
library(shinydashboard)

variables <- list( 'status','method', 'path')
interval <- list('minutos','segundos')
columns <- list('C_CONF','C_HOUR','C_MNTH','C_PERS','C_RALN','C_RCFG','C_RSUR','C_TRAF','C_VEHS','C_WDAY','C_WTHR','P_AGE','P_SAFE','P_SEX','V_AGE','V_TYPE')


body <- dashboardBody(
    fluidRow(
    box(width=3,title = "Inputs", status = "warning", solidHeader = TRUE,
    selectInput("graphRequestsBarInput", label = "Seleccionar filtro", choices = variables)
    ),
    box(title = "Bar plot",status = "primary", solidHeader = TRUE,plotOutput("graphRequestsBar"))
  ),
  fluidRow(
    box(width=3,title = "Inputs", status = "warning", solidHeader = TRUE,
    selectInput("graphRequestsSeriesInput", label = "Seleccionar intervalo de tiempo", choices = interval)
    ),
    box(title = "Series plot",status = "primary", solidHeader = TRUE,plotOutput("graphRequestsSeries"))
  ),
  fluidRow(
    box(width=3,title = "Inputs", status = "warning", solidHeader = TRUE,
    selectInput("graphPredictionBarInput", label = "Seleccionar categoria", choices = columns)
    ),
    box(title = "Predictions bar plot",status = "primary", solidHeader = TRUE,plotOutput("graphPredictionBar"))
  ),
  fluidRow(
    box(width=3,title = "Inputs", status = "warning", solidHeader = TRUE,
    sliderInput("graphPredictionInput", "Seleccionar numero de bins:", 5, 50, 5)
    ),
    box(title = "Prediction histogram",status = "primary", solidHeader = TRUE,plotOutput("graphPredictionHistProb"))
  )
)


shinyUI(
dashboardPage(
  dashboardHeader(title = "API Dashboard"),
  dashboardSidebar(disable = TRUE),
  body
)
)
