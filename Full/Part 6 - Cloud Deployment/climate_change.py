import pandas as pd
DATA_FOLDER = "../../data"
temperatures = pd.read_csv(f"{DATA_FOLDER}/global_temperatures/GlobalLandTemperaturesByCountry.csv", parse_dates=['dt'])
continents = pd.read_csv(f"{DATA_FOLDER}/continents.csv")
countries = pd.read_csv(f"{DATA_FOLDER}/countries.csv")
countries.drop(columns=['code'])
temperatures = temperatures.merge(continents).merge(countries, left_on="Country", right_on="country")

temperatures['year'] = temperatures.dt.dt.year
temperatures['month'] = temperatures.dt.dt.month

yearly_change = temperatures[(temperatures.year==1963) | (temperatures.year==2013)].groupby(["Country","year"], as_index=False).AverageTemperature.mean()
yearly_change['AverageTemperatureChange'] = yearly_change.groupby(["Country"], as_index=False).AverageTemperature.transform("diff")
yearly_change.dropna(inplace=True)
temperature_slice=yearly_change.merge(temperatures[["Country","Continent","Code","lon","lat"]].drop_duplicates())

import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def single_year(year=1950):
    df = temperatures[temperatures.year==year].groupby(["Country","year","Continent"]).mean().reset_index()
    df.AverageTemperatureUncertainty.fillna(0,inplace=True)
    return px.scatter(df, x="AverageTemperature", y="AverageTemperatureUncertainty", hover_name="Country", color="Continent", marginal_y="violin",marginal_x="histogram")

app.layout = html.Div(children=[
    html.H1(children='Global Temperatures'),

    html.Div(children='''
        Climate: A single year in the world
    '''),

    dcc.Graph(
        id='year-graph',
        figure=single_year()
    ),
    html.H1(
        id='range-year',
        children='1950'
    ),
    dcc.Slider(
        id='temperature-year',
        min=temperatures.year.min(),
        max=temperatures.year.max(),
        step=1,
        value=1950,
        marks={int(date):str(date) for date in temperatures.year.unique() if date%10==0}
    )
])

@app.callback(
    output=[
        Output(component_id="year-graph",component_property="figure"),
        Output(component_id="range-year",component_property="children")
    ],
    inputs=[
        Input(component_id="temperature-year", component_property="value")
    ]
)
def draw_country_history(year):
    figure = single_year(year)
    return figure, year

