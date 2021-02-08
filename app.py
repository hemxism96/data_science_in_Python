import dash
import pandas as pd
import numpy as np
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff
from myClass import myClass

import warnings
warnings.filterwarnings("ignore")

# data processing

# myClass is a python class that contains 4 functions for data processing. 
# This is to avoid a lot of repetitive code.
# Detailed function introduction is in myClass.py
datapro = myClass()

# First, perform data cleaning operations on the 4 CSV files respectively. 
# The documents are about Adolescent fertility, GDP, Secondary school enrollment, and Labor force female.
col_nameF = ['Country','Country Code','2014','2015','2016','2017','2018']
df_AF = datapro.getDataframe('data/Adolescent_fertility.csv',col_nameF,'Adolescent fertility')
df_GDP = datapro.getDataframe('data/GDP.csv',col_nameF,'GDP')
df_SES = datapro.getDataframe('data/School_enrollment_secondary.csv',col_nameF,'Secondary school enrollment')
df_LFF = datapro.getDataframe('data/Labor_force_female.csv',col_nameF,'Labor force female')

# In order to display the data more clearly and quickly, we can combine the two dataframes.
# In fact, this is not a simple combination. 
# Because each data file contains different countries with data, we need to do some filtering to keep the same country data.
df_AF_for_GDP = datapro.uniteDataframe(df_AF, df_GDP, 'GDP',0)
df_AF_for_SES = datapro.uniteDataframe(df_AF, df_SES, 'Secondary school enrollment',0)
df_AF_for_LFF = datapro.uniteDataframe(df_AF, df_LFF, 'Labor force female',0)
df_map = datapro.uniteDataframe(df_AF, "data/countries.csv", ' ',1)


# make graph by using Plotly

# Distribution of Adolescent fertility 2014-2018
hist_data = [df_AF['Adolescent fertility'][df_AF.Year=='2014'], df_AF['Adolescent fertility'][df_AF.Year=='2015'], df_AF['Adolescent fertility'][df_AF.Year=='2016'], df_AF['Adolescent fertility'][df_AF.Year=='2017'], df_AF['Adolescent fertility'][df_AF.Year=='2018']]
group_labels = ['2014','2015','2016','2017','2018']
fig_AF = ff.create_distplot(hist_data, group_labels, bin_size=5)
fig_AF.update_layout(title='Distribution of Adolescent fertility 2014-2018')

# Adolescent fertility vs GDP
dataframe = df_AF_for_GDP
data = dataframe.loc[:,["GDP","Adolescent fertility"]][df_AF_for_GDP.Year=='2018']
data["index"] = np.arange(1,len(data)+1)
fig_AF_vs_GDP = ff.create_scatterplotmatrix(data, diag='box', index='index',colormap='RdBu',
                                  colormap_type='cat',
                                  height=400, width=510)
fig_AF_vs_GDP.update_layout(title='Adolescent fertility vs GDP')

# Adolescent fertility vs Secondary school enrollment
fig_AF_vs_SES = px.scatter(df_AF_for_SES, x="Secondary school enrollment", y="Adolescent fertility", 
                    size="Adolescent fertility",hover_name="Country",color="Country Code",
                    animation_frame="Year",animation_group="Country",
                    size_max=35, height=400,width=750)
fig_AF_vs_SES.update_layout(title='Adolescent fertility vs Secondary school enrollment')

# Adolescent fertility vs Labor force female
p14 = go.Scatter(
                    x = df_AF_for_LFF['Labor force female'][df_AF_for_LFF.Year=='2014'],
                    y = df_AF_for_LFF['Adolescent fertility'][df_AF_for_LFF.Year=='2014'],
                    mode = "lines",
                    name = "2014",
                    marker = dict(color = 'green'),
                    text= df_AF_for_LFF.Country)
p15 = go.Scatter(
                    x = df_AF_for_LFF['Labor force female'][df_AF_for_LFF.Year=='2015'],
                    y = df_AF_for_LFF['Adolescent fertility'][df_AF_for_LFF.Year=='2015'],
                    mode = "lines",
                    name = "2015",
                    marker = dict(color = 'red'),
                    text= df_AF_for_LFF.Country)
p16 = go.Scatter(
                    x = df_AF_for_LFF['Labor force female'][df_AF_for_LFF.Year=='2016'],
                    y = df_AF_for_LFF['Adolescent fertility'][df_AF_for_LFF.Year=='2016'],
                    mode = "lines",
                    name = "2016",
                    marker = dict(color = 'violet'),
                    text= df_AF_for_LFF.Country)
p17 = go.Scatter(
                    x = df_AF_for_LFF['Labor force female'][df_AF_for_LFF.Year=='2017'],
                    y = df_AF_for_LFF['Adolescent fertility'][df_AF_for_LFF.Year=='2017'],
                    mode = "lines",
                    name = "2017",
                    marker = dict(color = 'blue'),
                    text= df_AF_for_LFF.Country)
p18 = go.Scatter(
                    x = df_AF_for_LFF['Labor force female'][df_AF_for_LFF.Year=='2018'],
                    y = df_AF_for_LFF['Adolescent fertility'][df_AF_for_LFF.Year=='2018'],
                    mode = "lines",
                    name = "2018",
                    marker = dict(color = 'black'),
                    text= df_AF_for_LFF.Country)
     
data = [p14, p15, p16, p17, p18]
properties = dict(title = 'Adolescent fertility vs Labor force female',
              xaxis= dict(title= 'Labor force female',ticklen= 5,zeroline= False),
             yaxis= dict(title= 'Adolescent fertility',ticklen= 5,zeroline= False),
             height=400
             )
fig_AF_vs_LFF = dict(data = data, layout = properties)

# Map of Adolescent fertility 2014-2018
fig_AF_map=px.scatter_mapbox(df_map,
        lon = 'lon',
        lat = 'lat',
        color = 'Adolescent fertility',
        size='Adolescent fertility',
        title="Map of Adolescent fertility 2014-2018",
        hover_name='Country',
        hover_data = ['Adolescent fertility'],
        animation_frame='Year',
        animation_group="Country",
        width=1370,height=550,
        color_continuous_scale = px.colors.diverging.Portland)
fig_AF_map.update_layout(
    mapbox=dict(
        accesstoken="pk.eyJ1IjoiaGFoaGEiLCJhIjoiY2tnc2V1MjhmMG13NjJ5bWZmYmMzajFzcyJ9.xLxuT4cGNMgP_Q5HXax6FA", #
        center=go.layout.mapbox.Center(lat=8, lon=17),
        zoom=1
    )
)


app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

# Create app layout
app.layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        dcc.Graph(
                            id="main_graph", 
                            figure=fig_AF
                        )
                    ],
                    className="pretty_container seven columns",
                ),
                html.Div(
                    [dcc.Graph(id="compare_graph",figure=fig_AF_vs_GDP)],
                    className="pretty_container five columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
            [
                html.Div(
                    [dcc.Graph(id="compare_graph2", figure=fig_AF_vs_SES)],
                    className="pretty_container seven columns",
                ),
                html.Div(
                    [dcc.Graph(id="compare_graph3", figure=fig_AF_vs_LFF)],
                    className="pretty_container five columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
            [
                html.Div(
                    [dcc.Graph(id="map_graph",figure=fig_AF_map)],
                ),

            ],
            className="row flex-display",
        ),
    ],
    id="mainContainer",
    style={"display": "flex", "flex-direction": "column"},
)


if __name__ == '__main__':
    app.run_server(debug=True)