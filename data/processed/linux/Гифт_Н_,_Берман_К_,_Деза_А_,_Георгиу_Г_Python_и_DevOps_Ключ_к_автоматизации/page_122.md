---
source_image: page_122.png
page_number: 122
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.58
tokens: 7442
characters: 1848
timestamp: 2025-12-24T03:03:59.875840
finish_reason: stop
---

Кластеризация методом k-средних

С помощью утилит командной строки можно реализовать и еще одну замечательную вещь — машинное обучение. В приведенном далее примере нам потребовалось всего несколько строк кода, чтобы создать функцию для кластеризации методом k-средних. В данном случае мы кластеризуем DataFrame Pandas на три кластера (по умолчанию):

def kmeans_cluster_housing(clusters=3):
    """Кластеризация DataFrame методом k-средних"""
    url = "https://raw.githubusercontent.com/noahgift/\n    socialpowernba/master/data/nba_2017_att_val_elo_win_housing.csv"
    val_housing_win_df = pd.read_csv(url)
    numerical_df = (
        val_housing_win_df.loc[:, ["TOTAL_ATTENDANCE_MILLIONS", "ELO",
        "VALUE_MILLIONS", "MEDIAN_HOME_PRICE_COUNTY_MILLIONS"]]
    )
    # Нормирование данных
    scaler = MinMaxScaler()
    scaler.fit(numerical_df)
    scaler.transform(numerical_df)
    # Кластеризация данных
    k_means = KMeans(n_clusters=clusters)
    kmeans = k_means.fit(scaler.transform(numerical_df))
    val_housing_win_df['cluster'] = kmeans.labels_
    return val_housing_win_df

Количество кластеров можно изменить на другое, передав нужный параметр с помощью click:

@cli.command()
@click.option("--num", default=3, help="number of clusters")
def cluster(num):
    df = kmeans_cluster_housing(clusters=num)
    click.echo("Clustered DataFrame")
    click.echo(df.head())

В итоге получаем кластеризованный DataFrame Pandas. Обратите внимание на наличие в нем столбца, отражающего распределение по кластерам:

$ python -W nuclearcli.py cluster
Clustered DataFrame
    TEAM   GMS   ...   COUNTY   cluster
0   Chicago Bulls   41   ...   Cook   0
1   Dallas Mavericks   41   ...   Dallas   0
2   Sacramento Kings   41   ...   Sacramento   1
3   Miami Heat   41   ...   Miami-Dade   0
4   Toronto Raptors   41   ...   York-County   0