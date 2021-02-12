import pandas as pd
from contextlib import contextmanager


def pp_imported_csv(csvfile):
  df = pd.read_csv(csvfile, keep_default_na=True)
  df.to_html(f'webui/templates/data.html',
             classes=["table-striped"], justify="left", na_rep="null", border=0)
  return df


def pp_err_imported_csv(csvdata, filename):
  df = pd.DataFrame(csvdata, columns=[
                    'AP MAC Address', 'Error'])
  df.to_html(f'webui/templates/err_{filename}.html',
             classes=["table-danger"], justify="center", na_rep="null", border=0)
  return df


def pp_formatted_csv(csvdata, filename):
  df = pd.DataFrame(csvdata, columns=[
                    'AP Name', 'AP MAC Address', 'Primary Controller', 'Policy Tag Name', 'Site Tag Name', 'RF Tag Name', 'Default Flag'])
  df.to_html(f'webui/templates/{filename}.html',
             classes=["table-striped"], justify="left", na_rep="null", border=0)
  return df


## Writing table data to html in memory
def pp_html_csv(csvdata, filename):
    df = pd.DataFrame(csvdata[0], columns=['AP Name', 'AP MAC Address', 'Primary Controller', 'Policy Tag Name', 'Site Tag Name', 'RF Tag Name', 'Default Flag'])

    @contextmanager
    def open_file(file, mode):
        f = open(file, mode)
        df_file = df.to_html(f, classes=["table-striped"], justify="left", na_rep="null", border=0)

        yield f

        os.remove(path)

    path = f'webui/templates/{filename}.html'

    with open_file(path, 'a+') as f:
      return df
