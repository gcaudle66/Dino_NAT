import luigi

# site scope
# import csv
# validate csv
# if single site-provide data
# 	data: ip/host, user/pass
# if multi site/dnac-provide data
# 	data: ip/host, user/pass
# connect ssh and validate
# 	collect inventory
# 	parse inventory and compare to csv
# 	send commands
# 	validate post
# 	disco
# 	REPEAT is necessary on next host
# save logs

# Define the objects for the flow


def set_apname_flow():
    who = dataset_objects
    what = Ap.apname
    when = local_scheduler
    where = Ap.pri_cntr
    why = flow_justification
    apname_flow = Flow()

class ImportCSV(luigi.Task):

    def requires(self):
        return []

    def output(self):
        return luigi.LocalTarget("output1.txt")

    def run(self):
        with self.output().open('w') as f:
            data = input("Please enter your name")
            f.write(data)

class ValidateCSV(luigi.Task):

    def requires(self):
        return [ImportCSV()]

    def output(self):
        return luigi.LocalTarget("output2.txt")

    def run(self):
        with self.input()[0].open() as fin, self.output().open('w') as fout:
            for line in fin:
                n = "sucks"
                fout.write(f"{line} {n}!!")


if __name__ == "__main__":
    luigi.run()
