import pandas as pd


def pp_imported_csv(csvfile, filename):
  df = pd.read_csv(csvfile, keep_default_na=True)
  df.to_html(f'webui/templates/{filename}.html',
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
                    'AP Name', 'AP MAC Address', 'Policy Tag Name', 'Site Tag Name', 'RF Tag Name'])
  df.to_html(f'webui/templates/{filename}.html',
             classes=["table-striped"], justify="left", na_rep="null", border=0)
  return df
