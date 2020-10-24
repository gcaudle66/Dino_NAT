import pandas as pd


def pp_imported_csv(csvfile):
    df = pd.read_csv(csvfile, keep_default_na=True)
    df.to_html('webui/templates/data.html',
               classes=["table-striped"], justify="left", na_rep="null", border=0)
    return df


def pp_formatted_csv(csvdata):
    df = pd.DataFrame(csvdata, columns=[
                      'AP Name', 'AP MAC Address', 'Policy Tag Name', 'Site Tag Name', 'RF Tag Name'])
    df.to_html('webui/templates/data.html',
               classes=["table-striped"], justify="left", na_rep="null", border=0)
    return df
