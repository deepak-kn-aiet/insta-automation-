export default function MessagesPage() {
  return (
    <section className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
      <h1 className="text-2xl font-semibold">Messages</h1>
      <p className="mt-2 text-sm text-slate-600">
        Incoming DM conversations will appear here.
      </p>
      <div className="mt-6 rounded-lg border border-dashed border-slate-300 p-8 text-center text-sm text-slate-500">
        No messages yet.
      </div>
    </section>
  );
}
