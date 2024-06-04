import json
from flask import Flask, request, jsonify
from autogenstudio import AgentWorkFlowConfig, AutoGenWorkFlowManager

# Initialize Flask app
app = Flask(__name__)

# Load the agent specification in JSON
agent_spec = json.load(open("C:/Users/hp/Downloads/workflow_travel.json"))

# Create an AutoGen Workflow Configuration from the agent specification
agent_work_flow_config = AgentWorkFlowConfig(**agent_spec)
agent_work_flow = AutoGenWorkFlowManager(agent_work_flow_config)

@app.route('/run_workflow', methods=['POST'])
def run_workflow():
    # Get the task query from the request data
    data = request.json
    task_query = data.get('task_query')
    
    if not task_query:
        return jsonify({'error': 'Task query is required'}), 400

    # Run the workflow on the task
    result = agent_work_flow.run(message=task_query)

    # Return the result as a JSON response
    response = agent_work_flow.agent_history[-1]["message"]["content"]
    return {
        "response":response
    }

if __name__ == '__main__':
    app.run(debug=True)
