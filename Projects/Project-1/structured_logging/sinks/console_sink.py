from structured_logging.sinks.i_sink import ISink
import json

class ConsoleSink(ISink):
    def sink_data(self, data):
        # data_len = len(data)
        # i = 0
        # strings: list[str] = ["{"]

        # for key, value in data.items():
        #     i += 1
        #     string = f'  "{key}": "{value}"'
        #     if i < data_len:
        #         string += ","
        #     strings.append(string)
        # strings.append("}")

        # print("\n".join(strings))

        print(json.dumps(data, indent=2, ensure_ascii=False))
