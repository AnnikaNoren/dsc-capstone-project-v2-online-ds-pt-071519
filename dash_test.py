import dash
import dash_core_components as dcc 
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go 
import base64

# Read in dataframe 
df = pd.read_csv('cleaned_coffee_reviews.csv')
df = df.drop(columns=['Unnamed: 0.1','Unnamed: 0.1.1','Unnamed: 0'], axis=1)


# scatter plot #1
trace = go.Scatter(x=df["Rating"], y=df["Prices Per Oz"], mode='markers')
fig = go.Figure(data=trace)
coffee_graph = dcc.Graph(figure=fig)
fig.update_traces(textposition='top center')
fig.update_layout(height=1000,title_text='Rating vs Prices Per Oz')

#  bar plot #2
#  https://pbpython.com/plotly-dash-intro.html
trace2 = go.Bar(x=df['Rating'], y=df['Prices Per Oz'])

# Drop down menu options
features = df[['Flavor','Body','Aroma','Aftertaste','Acidity','Prices Per Oz','Agtron Ground']].copy()
opts = [{'label' : i, 'value' : i} for i in features]

# Main App
app = dash.Dash()

app.layout = html.Div(children=[
    html.Div([
        html.H1('Finding The Perfect Cup of Coffee'),
        html.P('Annika M Noren, May 2020')],
        style = {'padding' : '50px' , 
                 'backgroundColor' : '#907A1C'}),
    coffee_graph,
    dcc.Graph(
        id='second plot',
        figure={
            'data': [trace2],
            'layout': go.Layout(
                title='Second Plot', 
                xaxis = {'title':'Rating'},
                yaxis = {'title':'Price'},
                barmode='stack')})
])



if __name__ == '__main__':
    app.run_server(debug = True)




# Extra Code that is obsolete, didn't work or not needed

# Helpful tutorial: https://www.youtube.com/watch?v=hRH01ZzT2NI

# Bean image, couldn't get it bigger
# image_filename = 'beans_leaf.jpeg' # replace with your own image
# encoded_image = base64.b64encode(open(image_filename, 'rb').read())
# html.Img(src='data:image/png;base64,{}, style={'width':'20%'}'.format(encoded_image))


# app.layout = html.Div('Coffee')

# app.layout = html.Div(children=[
#     html.H1('The Perfect Cup of Coffee'),
#     coffee_graph,
#     dcc.Graph(
#         id='second plot',
#         figure={
#             'data': [trace2],
#             'layout': go.Layout(title='Second Plot', barmode='stack')
#         }
#     )
# ])

# app.layout = html.Div([
#                 # adding a header and a paragraph
#                 html.Div([
#                     html.H1("Finding the Perfect Cup of Coffee")], 
#                     style = {'padding' : '50px' , 
#                              'backgroundColor' : '#907A1C'})
# ])