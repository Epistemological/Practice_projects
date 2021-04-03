import datetime
import dash
import dash_html_components as html
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from teledata_dashboard.apps import app_all_data, app_big_4, app_other_carriers, app_boniro
from teledata_dashboard import index
import dash_table
from dash.dependencies import Input, Output
import dash_daq as daq
import dash_bootstrap_components as dbc
import pandas as pd
import pathlib

date_version = ['Latest update: 2021-02-11, v1.0.0']

app_color = {
    'background':'#09385d',
    'text': '#edf5e0',
    'carrier_plt_public': '#edf5e0'}


app = dash.Dash(__name__, suppress_callback_exceptions=True)

test_data = pd.read_csv('C:/Users/Dennis Besseling/PycharmProjects/work_projects/practice_dashboards/test_file.csv')

def serve_layout():
    ''' function to enable update of site data when browser is updated by user '''
    dt = datetime.datetime.now().strftime('%Y-%m-%d')
    #PATH = pathlib.Path(__file__).parent
    #DATA_PATH = PATH.joinpath('../OPSTATS/existing_data').resolve()
    df_pb = pd.read_csv('C:/Users/Dennis Besseling/PycharmProjects/work_projects/teledata_dashboard/OPSTATS/existing_data/pb_data.csv', sep=',')
    df_org = pd.read_csv('C:/Users/Dennis Besseling/PycharmProjects/work_projects/teledata_dashboard/OPSTATS/existing_data/org_data.csv', sep=',')
    df_all_sep = pd.read_csv('C:/Users/Dennis Besseling/PycharmProjects/work_projects/teledata_dashboard/OPSTATS/existing_data/carrier_all_sep.csv', sep=',')
    df_mob_sep = pd.read_csv('C:/Users/Dennis Besseling/PycharmProjects/work_projects/teledata_dashboard/OPSTATS/existing_data/carrier_mob_sep.csv', sep=',')
    df_std_sep = pd.read_csv('C:/Users/Dennis Besseling/PycharmProjects/work_projects/teledata_dashboard/OPSTATS/existing_data/carrier_std_sep.csv', sep=',')
    df_org_sep = pd.read_csv('C:/Users/Dennis Besseling/PycharmProjects/work_projects/teledata_dashboard/OPSTATS/existing_data/carrier_org_sep.csv', sep=',')
    df_pb_sep = pd.read_csv('C:/Users/Dennis Besseling/PycharmProjects/work_projects/teledata_dashboard/OPSTATS/existing_data/carrier_pb_sep.csv', sep=',')
    list_of_frames = [df_pb, df_org]
    public_data = pd.concat(list_of_frames, ignore_index=True)
    graph_df = pd.DataFrame(data={'date': df_pb['date'],
                                  'private mobile': df_pb['mobile'],
                                  'private landline': df_pb['landline'],
                                  'private total': df_pb['total'],
                                  'company mobile': df_org['mobile'],
                                  'company landline': df_org['landline'],
                                  'company total': df_org['total'],
                                  'mobile total': df_pb['mobile'] + df_org['mobile'],
                                  'landline total': df_pb['landline'] + df_org['landline'],
                                  'total': df_pb['total'] + df_org['total']})

    all_carrier_sep_df = df_all_sep[df_all_sep.columns[:-3]]

    all_carrier_sep_df = pd.DataFrame(data={'Carriers': all_carrier_sep_df.columns,
                                            'all subs': all_carrier_sep_df.iloc[-1]})


    all_carrier_sep_df = all_carrier_sep_df.sort_values(by='all subs')

    fig = px.bar(all_carrier_sep_df, y='Carriers', x='all subs', orientation='h', height=2500, text='all subs')
    fig.update_traces(textposition='auto')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide',
                      title={'text': 'Amount of carriers:',
                             'font': {'size': 20},
                             'y': 0.985,
                             'x': 0.6,
                             'xanchor': 'center'},
                      yaxis={'title': 'Carrier'},
                      xaxis={'title': 'Amount of subscriptions'},
                      paper_bgcolor='lightblue'
                      )
    number_of_carriers = len(df_all_sep.keys()[:-3])
    graph_date = df_all_sep['date'].iloc[-1]


    header = index.header

    page_1_layout = index.page_1_layout

    page_2_layout = index.page_2_layout

    page_3_layout = index.page_3_layout

    page_4_layout = index.page_4_layout

    page_5_layout = index.page_5_layout

    teledata_db = html.Div([
            dcc.Location(id='url', refresh=False),
                               html.Div(id='page-content')
                               ])

    @app.callback(Output('page-content', 'children'),
                  [Input('url', 'pathname')])
    def display_page(pathname):
        if pathname == '/all_data':
            return page_1_layout
        elif pathname == '/largest_carriers':
            return page_2_layout
        elif pathname == '/other_carriers':
            return page_3_layout
        elif pathname == '/boniro_comp':
            return page_4_layout
        elif pathname == '/boniro_pb':
            return page_5_layout
        elif pathname == '/':
            return header
        else:
            return "Woops! This page doesn't exist yet. Please try again."

    return teledata_db




app.layout = serve_layout



if __name__ == '__main__':
    app.run_server(debug=True)