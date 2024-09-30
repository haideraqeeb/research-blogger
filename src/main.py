from flask import Flask, request
from gpt_researcher import GPTResearcher
import asyncio

app = Flask(__name__)


@app.route("/report/<report_type>", methods=["GET"])
async def get_report(report_type):
    query = request.args.get('query')
    researcher = GPTResearcher(query, report_type)
    research_result = await researcher.conduct_research()
    report = await researcher.write_report()
    return report

if (__name__ == "__main__"):
    app.run(debug=True)
