import { useHealth } from '../hooks/useHealth';

export default function StatusCard() {
  const { data, isLoading } = useHealth();

  return (
    <div className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
      <p className="text-sm text-slate-500">Backend Status</p>
      {isLoading ? <p className="mt-2 text-sm">Loading...</p> : <p className="mt-2 font-semibold">{data?.status}</p>}
    </div>
  );
}
